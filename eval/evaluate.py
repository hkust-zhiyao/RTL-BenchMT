#!/usr/bin/env python3
"""RTL-BenchMT universal evaluation CLI.

Run an LLM against a benchmark and an iverilog/cocotb simulator, comparing
performance on `original` vs `fixed` prompts.

Quick start:
    # smoke test on 3 V1 cases with a stub LLM (canonical-as-DUT)
    python3 eval/evaluate.py --bench verilogeval_human_v1 --variant fixed \\
        --llm canonical --simulator iverilog --limit 3

    # real run with HKUST Azure GPT-4o-mini
    python3 eval/evaluate.py --bench verilogeval_human_v1 --variant fixed \\
        --llm azure_gpt4o_mini --simulator iverilog \\
        --output results/v1_fixed.jsonl

Outputs one JSON line per task to --output (or stdout). Use --summarize
on a results file to get per-bench / per-type / Δ aggregates.
"""

import argparse
import json
import sys
import tempfile
import time
from pathlib import Path

# Make the package importable when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from eval.loader import load_bench, get_id, ALL_BENCHES, get_dut_name
from eval.prompt_builder import build_prompt, has_variant
from eval.code_extraction import extract_verilog


# ── LLM registry ─────────────────────────────────────────────────────────

def _make_llm(name: str):
    """Lazy import + construct an LLM caller by short name."""
    if name == "azure_gpt4o_mini":
        from eval.llm.azure_gpt import AzureGPT
        return AzureGPT(model="gpt-4o-mini")
    if name == "azure_gpt4o":
        from eval.llm.azure_gpt import AzureGPT
        return AzureGPT(model="gpt-4o")
    if name == "canonical":
        return _CanonicalLLM()
    if name == "stub":
        from eval.llm.stub import CustomLLM
        return CustomLLM()
    raise ValueError(
        f"unknown --llm '{name}'. built-in: azure_gpt4o_mini, azure_gpt4o, "
        f"canonical, stub. To add your own, edit eval/evaluate.py "
        f"_make_llm() and follow eval/llm/stub.py."
    )


class _CanonicalLLM:
    """Cheats: returns the record's canonical solution. Used to sanity-test
    the simulator pipeline without burning API credits."""

    name = "canonical"

    def __call__(self, prompt: str, system_prompt=None) -> str:
        # The CLI sets self._record before calling.
        bench = self._bench
        r = self._record
        if bench.startswith("cvdp_"):
            harness = r.get("harness", {}).get("files", {})
            for k, v in harness.items():
                if isinstance(v, str) and (k.endswith(".sv") or k.endswith(".v")):
                    return f"```verilog\n{v}\n```"
            return "```verilog\n// no canonical available for cvdp\n```"
        if bench == "rtllm_v1.1":
            return f"```verilog\n{r.get('verified', '')}\n```"
        if bench == "verilogeval_human_v2":
            ref = r.get("reference", "").replace("RefModule", "TopModule")
            return f"```verilog\n{ref}\n```"
        # V1 / Machine v1
        return f"```verilog\n{r.get('prompt', '') + r.get('canonical_solution', '')}\n```"


# ── Simulator registry ───────────────────────────────────────────────────

def _make_simulator(name: str):
    if name == "iverilog":
        from eval.simulators.iverilog import IverilogSimulator
        return IverilogSimulator()
    if name == "cocotb_iverilog":
        from eval.simulators.cocotb_iverilog import CocotbIverilogSimulator
        return CocotbIverilogSimulator()
    raise ValueError(
        f"unknown --simulator '{name}'. built-in: iverilog, cocotb_iverilog."
    )


def _default_simulator_for(bench: str) -> str:
    return "cocotb_iverilog" if bench.startswith("cvdp_") else "iverilog"


# ── eval loop ────────────────────────────────────────────────────────────

def _eval_one(record, bench, variant, llm, simulator, work_dir):
    sys_p, user_p = build_prompt(bench, record, variant=variant)
    # Hook for the canonical pseudo-LLM.
    if isinstance(llm, _CanonicalLLM):
        llm._bench = bench
        llm._record = record

    t0 = time.time()
    try:
        response = llm(user_p, system_prompt=sys_p)
    except Exception as e:
        return {
            "passed": False, "stage": "llm", "error": f"LLM error: {e}",
            "prompt_chars": len(user_p), "response_chars": 0,
            "duration_s": time.time() - t0,
        }

    code = extract_verilog(response)
    sim_result = simulator.run(code, record, work_dir, bench)

    return {
        "passed": sim_result.passed,
        "stage": sim_result.stage,
        "error": sim_result.error,
        "output": (sim_result.output or "")[-2000:],
        "prompt_chars": len(user_p),
        "response_chars": len(response),
        "extracted_chars": len(code),
        "duration_s": time.time() - t0,
    }


# ── CLI ──────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bench", required=False, choices=ALL_BENCHES,
                    help="benchmark to evaluate")
    ap.add_argument("--variant", choices=["original", "fixed"], default="fixed",
                    help="which prompt to send to the LLM")
    ap.add_argument("--llm", default="azure_gpt4o_mini",
                    help="LLM caller (azure_gpt4o_mini | azure_gpt4o | "
                         "canonical | stub | <your custom>)")
    ap.add_argument("--simulator", default=None,
                    help="iverilog | cocotb_iverilog (default: per-bench)")
    ap.add_argument("--output", type=Path, default=None,
                    help="write JSONL results here; default: stdout")
    ap.add_argument("--limit", type=int, default=None,
                    help="evaluate at most N tasks")
    ap.add_argument("--task-ids", default=None,
                    help="comma-separated subset of task ids")
    ap.add_argument("--only-fixed-records", action="store_true",
                    help="restrict to ambiguity_fixed=True records (for "
                         "comparison runs).")
    ap.add_argument("--summarize", type=Path, default=None,
                    help="instead of running, print summary of a results.jsonl")

    args = ap.parse_args()

    if args.summarize:
        return _summarize(args.summarize)

    if not args.bench:
        ap.error("--bench is required (unless using --summarize)")

    sim_name = args.simulator or _default_simulator_for(args.bench)

    records = load_bench(args.bench)
    if args.only_fixed_records or args.variant == "original":
        # When comparing original vs fixed, both runs should target the
        # same task set (only those that have a fix). For original variant
        # of an unfixed record, the prompt is just the upstream prompt —
        # which is fine, but typically you want to restrict to the fixed
        # subset for paper-style comparison.
        records = [r for r in records if r.get("ambiguity_fixed", False)]
    if args.task_ids:
        wanted = set(args.task_ids.split(","))
        records = [r for r in records if get_id(args.bench, r) in wanted]
    if args.limit is not None:
        records = records[:args.limit]
    if not records:
        print("no records to evaluate after filtering", file=sys.stderr)
        sys.exit(1)

    llm = _make_llm(args.llm)
    sim = _make_simulator(sim_name)

    out_fh = open(args.output, "w") if args.output else sys.stdout
    n_pass, n_fail, n_total = 0, 0, 0

    try:
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            for i, r in enumerate(records):
                tid = get_id(args.bench, r)
                if not has_variant(r, args.variant):
                    print(f"skip {tid}: no '{args.variant}' variant",
                          file=sys.stderr)
                    continue
                work = tmp / f"case_{i:04d}"
                res = _eval_one(r, args.bench, args.variant, llm, sim, work)
                rec = {
                    "bench": args.bench,
                    "task_id": tid,
                    "variant": args.variant,
                    "ambiguity_type": r.get("ambiguity_type", ""),
                    "llm": getattr(llm, "name", args.llm),
                    "simulator": sim.name,
                    **res,
                }
                out_fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                out_fh.flush()
                n_total += 1
                if res["passed"]:
                    n_pass += 1
                else:
                    n_fail += 1
                # Progress to stderr
                mark = "PASS" if res["passed"] else f"FAIL ({res.get('stage','?')})"
                print(f"[{i+1}/{len(records)}] {tid:36s} {args.variant:8s} "
                      f"{mark:14s} {res['duration_s']:5.1f}s", file=sys.stderr)
    finally:
        if args.output:
            out_fh.close()

    print(f"\nDone: {n_pass}/{n_total} passed ({100*n_pass/max(n_total,1):.1f}%)",
          file=sys.stderr)


def _summarize(path: Path):
    rows = [json.loads(l) for l in open(path)]
    by_key = {}  # (bench, variant, ambiguity_type) -> [pass, total]
    for r in rows:
        k = (r["bench"], r["variant"], r.get("ambiguity_type") or "—")
        c = by_key.setdefault(k, [0, 0])
        c[1] += 1
        if r.get("passed"):
            c[0] += 1
    print(f"{'bench':24s} {'variant':10s} {'type':12s} {'pass/total':>12s} {'rate':>8s}")
    for (b, v, t), (p, n) in sorted(by_key.items()):
        rate = f"{100*p/n:.1f}%" if n else "—"
        print(f"{b:24s} {v:10s} {t:12s} {p:>5d}/{n:<6d} {rate:>8s}")

    # Δ summary if both variants present
    print("\nΔ (fixed - original) by bench:")
    benches = sorted({r["bench"] for r in rows})
    for b in benches:
        rows_b = [r for r in rows if r["bench"] == b]
        n_orig = sum(1 for r in rows_b if r["variant"] == "original")
        p_orig = sum(1 for r in rows_b if r["variant"] == "original" and r["passed"])
        n_fix = sum(1 for r in rows_b if r["variant"] == "fixed")
        p_fix = sum(1 for r in rows_b if r["variant"] == "fixed" and r["passed"])
        if n_orig and n_fix:
            d = 100*p_fix/n_fix - 100*p_orig/n_orig
            print(f"  {b:24s} original={p_orig}/{n_orig}={100*p_orig/n_orig:.1f}%, "
                  f"fixed={p_fix}/{n_fix}={100*p_fix/n_fix:.1f}%, Δ={d:+.1f}pp")


if __name__ == "__main__":
    main()
