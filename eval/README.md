# RTL-BenchMT Evaluation

A pluggable evaluation framework for the six RTL-BenchMT benchmarks. Send a
prompt to your LLM, parse out the Verilog, run it under iverilog (or any
other simulator), and compare pass rate on the original vs the revised
prompt. Designed so you can swap in any LLM backend and any simulator.

## Installation

Pick **one** of the two install paths below.

### Path A — conda (recommended; bundles iverilog + cocotb)

```bash
conda env create -f environment.yml
conda activate rtl-benchmt-eval
```

This installs Python, iverilog, make, cocotb, and openai in a single
isolated environment.

### Path B — pip + system iverilog

```bash
# Python deps
pip install -r requirements.txt
# System deps (Debian/Ubuntu)
sudo apt-get install iverilog make
# macOS
# brew install icarus-verilog
```

If you don't plan to evaluate the CVDP benchmarks, you can skip cocotb and
make — VerilogEval and RTLLM only need `iverilog` and `openai`.

### Verify

```bash
iverilog -V                               # should print "Icarus Verilog 11.x"
python3 -c "import openai, cocotb"        # should print nothing (no errors)
```

## Quick start

```bash
# 1. Configure your API key
cp eval/config/openai-api-list.txt.example eval/config/openai-api-list.txt
# then edit it: one Azure OpenAI key per line

# 2. Smoke test with the canonical pseudo-LLM (no API needed)
python3 eval/evaluate.py --bench verilogeval_human_v1 --variant fixed \
    --llm canonical --only-fixed-records --limit 3

# 3. Real run with GPT-4o-mini on the V1 fixed prompts
python3 eval/evaluate.py --bench verilogeval_human_v1 --variant fixed \
    --llm azure_gpt4o_mini --only-fixed-records \
    --output results/v1_fixed.jsonl

# 4. Compare against original V1 prompts
python3 eval/evaluate.py --bench verilogeval_human_v1 --variant original \
    --llm azure_gpt4o_mini --only-fixed-records \
    --output results/v1_original.jsonl

# 5. Aggregate
cat results/*.jsonl > results/all.jsonl
python3 eval/evaluate.py --summarize results/all.jsonl
```

## CLI flags

| flag | meaning |
|---|---|
| `--bench` | `verilogeval_human_v1` / `verilogeval_human_v2` / `verilogeval_machine_v1` / `rtllm_v1.1` / `cvdp_cid002` / `cvdp_cid003` |
| `--variant` | `fixed` (revised by the agentic pipeline) or `original` (upstream) |
| `--llm` | `azure_gpt4o_mini` / `azure_gpt4o` / `canonical` (cheats, sanity-test) / `stub` / your own (see below) |
| `--simulator` | `iverilog` (default for VE / RTLLM) / `cocotb_iverilog` (default for CVDP) / your own |
| `--output` | JSONL file to write per-task results to (default: stdout) |
| `--limit N` | run at most N tasks |
| `--task-ids id1,id2` | run only the listed task IDs |
| `--only-fixed-records` | restrict to records with `ambiguity_fixed=true` (the comparable subset) |
| `--summarize FILE` | aggregate a results JSONL instead of running |

## Plugging in your own LLM

The `LLMCaller` protocol is one method:

```python
class MyLLM:
    name = "my_llm"
    def __call__(self, prompt: str, system_prompt: str | None = None) -> str:
        # call your model and return its text response
        ...
```

Drop it in `eval/llm/my_llm.py`, then register it in `eval/evaluate.py` by
adding a branch to `_make_llm()`. See `eval/llm/azure_gpt.py` for a
concrete OpenAI-compatible example and `eval/llm/stub.py` for a starter.

## Plugging in your own simulator

Same pattern. The `Simulator` protocol returns a `SimResult` with at least
`passed: bool`. Add `eval/simulators/my_sim.py` and register it in
`_make_simulator()`. See `eval/simulators/iverilog.py` for the iverilog
reference and `eval/simulators/cocotb_iverilog.py` for the cocotb wrapper.

## Per-benchmark spec construction

What the LLM actually sees, per benchmark:

| benchmark | LLM-visible prompt |
|---|---|
| VerilogEval Human v1 | `detail_description + "\n\n" + prompt` |
| VerilogEval Human v2 | `instruction` |
| VerilogEval Machine v1 | `detail_description + "\n\n" + prompt` (same layout as Human v1) |
| RTLLM v1.1 | `design_prompt` |
| CVDP cid002 / cid003 | `input.prompt` |

When `--variant fixed`, the framework reads the revised field; when
`--variant original`, it reads the upstream field (`original_*` if
present). See `eval/prompt_builder.py` for the exact mapping.

## Pass criteria

Defaults the `iverilog` simulator uses:

- **VerilogEval (Human v1, v2, Machine v1)**: testbench prints
  `Mismatches: 0 in N samples` with N > 0.
- **RTLLM v1.1**: testbench prints a conventional pass marker
  (`Your Design Passed`, `Test passed`, `error = 0`) with no fail marker.
- **CVDP** (cocotb): pass iff `results.xml` has at least one `<testcase>`
  and zero `<failure>` / `<error>` children.

## Layout

```
eval/
├── README.md                       (this file)
├── evaluate.py                     CLI entrypoint
├── loader.py                       loads datasets/<bench>.{json,jsonl}
├── prompt_builder.py               per-benchmark spec construction
├── code_extraction.py              pull Verilog from LLM response
├── llm/
│   ├── base.py                     LLMCaller protocol
│   ├── azure_gpt.py                HKUST Azure OpenAI example
│   └── stub.py                     template for your own backend
├── simulators/
│   ├── base.py                     Simulator protocol
│   ├── iverilog.py                 default for VerilogEval / RTLLM
│   └── cocotb_iverilog.py          default for CVDP
└── config/
    └── openai-api-list.txt.example one API key per line; first usable is read
```

## Notes

- All runs are pass@1 with `temperature=0` for reproducibility. To change,
  edit your LLM caller's constructor.
- iverilog must be on `PATH`. cocotb is only needed if you evaluate the
  CVDP benchmarks (`cvdp_cid002` / `cvdp_cid003`).
- The default Azure endpoint is HKUST's proxy
  (`https://hkust.azure-api.net/`, api version `2024-10-21`). Override with
  `AZURE_OPENAI_ENDPOINT` / `AZURE_OPENAI_API_VERSION` env vars or by
  constructing `AzureGPT(...)` with explicit kwargs.
