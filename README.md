# RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmark Through Agent-Assisted Analysis and Revision

Companion dataset and evaluation code for the DAC 2026 paper:

> **RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmark Through Agent-Assisted Analysis and Revision**
> Jing Wang, Shang Liu, Hangan Zhou, Zhiyao Xie

## Status

**Released.** The revised benchmark files, the per-case analysis tree, and a unified evaluation script are all in this repository. We covered six upstream RTL-generation benchmarks; an agentic pipeline identified and repaired 47 cases with concrete prompt ambiguities. For each repaired case, the original prompt is preserved alongside the revised prompt so users can compare model behavior directly.

## Motivation

LLM-assisted automated RTL generation is one of the most important directions in EDA research, where LLMs generate the desired RTL design from a natural-language description. These works rely on open RTL benchmarks to measure functional correctness and compare models.

Existing RTL benchmarks, however, inevitably contain flawed cases that misrepresent the true capability of LLMs. Some tasks exhibit inconsistencies between the design description and the reference testbench. Others omit critical implementation details, such as reset polarity, initial register values, or one-hot state encodings. Such flaws cause otherwise correct designs to be marked as failures, leading to unfair or misleading evaluation. Systematically identifying and revising flawed cases across large benchmarks is highly labor-intensive and requires substantial RTL and verification expertise.

RTL-BenchMT is an agentic framework that automates this maintenance: it identifies flawed benchmark cases and proposes minimally-revised descriptions that resolve the ambiguity while preserving the upstream task. This repository releases the agentic-pipeline outputs — for every fixed case, the original prompt is preserved alongside the revised prompt, with a per-case rationale, and a unified evaluation script that can compare model behavior on both.

## What this repository provides

- **[datasets/](datasets/)** — six revised dataset files. Every record carries `original_*` (upstream prompt verbatim) and the revised field. Records with `ambiguity_fixed: true` are the ones the agentic pipeline modified; everything else is upstream-as-is.
- **[per-case-analysis/](per-case-analysis/)** — one folder per fixed case with `original.txt`, `fixed.txt`, and `analysis.md` so you can read the diff and the rationale at a glance.
- **[eval/](eval/)** — a unified evaluation script that runs any LLM against any of the six benchmarks under iverilog (or cocotb for CVDP). LLM backend and simulator are both pluggable. See [eval/README.md](eval/README.md).
- **[results/](results/)** — sample `--limit` smoke-test JSONL produced by the eval script, included as a sanity reference for the output schema.

## Benchmark status

| Benchmark | Total tasks | Repaired |
|---|---:|---:|
| VerilogEval Human v1 | 156 | 14 |
| VerilogEval Human v2 | 156 | 8 |
| VerilogEval Machine v1 | 143 | 11 |
| RTLLM v1.1 | 50 | 5 |
| CVDP cid002 | 94 | 4 |
| CVDP cid003 | 77 | 5 |
| **Total** | **676** | **47** |

Each repaired record carries an `ambiguity_type` field (one of `functional`, `syntax`, `diagram`) and a `fix_description` string. See [per-case-analysis/](per-case-analysis/) for the per-case rationale and the original-vs-fixed diff.

## How we evaluate

Each benchmark has its own prompt-construction convention. The eval script normalizes them:

| Benchmark | What the LLM sees | Simulator |
|---|---|---|
| VerilogEval Human v1 / Machine v1 | `detail_description + module_header` | iverilog |
| VerilogEval Human v2 | `instruction` | iverilog |
| RTLLM v1.1 | `design_prompt` | iverilog |
| CVDP cid002 / cid003 | `input.prompt` (often a partial template) | cocotb (with iverilog backend) |

The `--variant` flag chooses between `original` and `fixed` so you can run the same LLM twice and compare pass rates directly. Pass criterion is the upstream convention for each benchmark (mismatch count for VerilogEval, conventional pass markers for RTLLM, cocotb's `results.xml` for CVDP).

For full instructions including install, the LLM/simulator plugin contracts, and the CLI flags, see **[eval/README.md](eval/README.md)**.

Quick start:

```bash
# install (one of)
conda env create -f environment.yml && conda activate rtl-benchmt-eval
# or
pip install -r requirements.txt && sudo apt-get install iverilog

# example: run GPT-4o-mini on the V1 fixed prompts
cp eval/config/openai-api-list.txt.example eval/config/openai-api-list.txt
# put your Azure key in that file
python3 eval/evaluate.py --bench verilogeval_human_v1 --variant fixed \
    --llm azure_gpt4o_mini --only-fixed-records --output results/v1_fixed.jsonl
```

## Citation

```bibtex
@inproceedings{wang2026rtlbenchmt,
  title={RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmark Through Agent-Assisted Analysis and Revision},
  author={Wang, Jing and Liu, Shang and Zhou, Hangan and Xie, Zhiyao},
  booktitle={Proceedings of the Design Automation Conference (DAC)},
  year={2026}
}
```

## License

The revised prompts are released under the same licenses as the upstream benchmarks (VerilogEval, RTLLM, CVDP). Refer to the original benchmark repositories for license terms.
