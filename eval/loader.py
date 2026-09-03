"""Load RTL-BenchMT records from datasets/."""

import json
from pathlib import Path

DATASETS = Path(__file__).resolve().parent.parent / "datasets"

BENCH_FILES = {
    "verilogeval_human_v1":   DATASETS / "verilogeval_human_v1.json",
    "verilogeval_human_v2":   DATASETS / "verilogeval_human_v2.json",
    "verilogeval_machine_v1": DATASETS / "verilogeval_machine_v1.json",
    "rtllm_v2.1":             DATASETS / "rtllm_v2.1.json",
    "cvdp_cid002":            DATASETS / "cvdp_cid002.jsonl",
    "cvdp_cid003":            DATASETS / "cvdp_cid003.jsonl",
}

ALL_BENCHES = list(BENCH_FILES)


def load_bench(bench):
    p = BENCH_FILES[bench]
    if p.suffix == ".jsonl":
        return [json.loads(l) for l in open(p)]
    return json.load(open(p))


def get_id(bench, record):
    if bench.startswith("cvdp_"):
        return record.get("id", "")
    if bench == "rtllm_v2.1":
        return record.get("design_name", "")
    return record.get("name") or record.get("task_id") or ""


def get_dut_name(bench, record):
    """Module name the testbench expects to instantiate."""
    if bench == "rtllm_v2.1":
        return record.get("design_name", "")
    if bench == "verilogeval_human_v2":
        return "TopModule"
    if bench in ("verilogeval_human_v1", "verilogeval_machine_v1"):
        return "top_module"
    if bench.startswith("cvdp_"):
        # CVDP module name is taken from the cocotb harness; the test runner
        # discovers it. Most cases follow id pattern cvdp_copilot_<name>_NNNN.
        tid = record.get("id", "")
        m = tid.replace("cvdp_copilot_", "").rsplit("_", 1)
        return m[0] if m else tid
    return ""
