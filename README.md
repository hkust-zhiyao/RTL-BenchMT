# RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmarks Through Agentic Framework with Formal-Validation-Based Guidance

Dataset and evaluation code for RTL-BenchMT. Version 1.0 accompanies the DAC 2026 paper:

> **RTL-BenchMT: Dynamic Maintenance of RTL Generation Benchmark Through Agent-Assisted Analysis and Revision**
> Jing Wang, Shang Liu, Hangan Zhou, Zhiyao Xie

## Status

**Version 2.0 released.** This version aligns with our extended work. It introduces formal-validation-based guidance through SpecIR, supports three benchmark-maintenance applications, and adds 438 expanded RTL variants. Across six RTL-generation benchmarks, RTL-BenchMT identifies and repairs 47 cases with concrete prompt ambiguities. The jointly developed flaw fixes for RTLLM are also incorporated into RTLLM v2.1 as a benchmark refinement contribution.

**Version 1.0** introduced the original agent-assisted benchmark-maintenance framework and was accepted at DAC 2026. For every repaired case, this repository preserves the original prompt alongside the revised prompt so users can compare model behavior directly.

## Motivation

RTL generation benchmarks are essential for evaluating LLM-based RTL design, but they face three persistent challenges: flawed cases can distort evaluation, public and static cases create overfitting risks, and limited benchmark scale restricts functional diversity. Maintaining these benchmarks manually requires substantial hardware-design and verification effort.

RTL-BenchMT addresses these challenges through three applications: **(1) flawed case identification and revision**, **(2) overfitting detection and updating**, and **(3) benchmark expansion**. SpecIR provides formal-validation-based guidance for agentic observation and reasoning, while human engineers review the suggested revisions and expansions before release.

## What this repository provides

- **[datasets/](datasets/)** — six revised dataset files. Every repaired record carries an `original_*` field alongside the revised field. Records with `ambiguity_fixed: true` are the ones the agentic pipeline modified. The jointly developed RTLLM flaw fixes are included here and are also released in RTLLM v2.1.
- **[per-case-analysis/](per-case-analysis/)** — one folder per fixed case with `original.txt`, `fixed.txt`, and `analysis.md` so you can read the diff and the rationale at a glance.
- **[expanded_cases/by_source/](expanded_cases/by_source/)** — 438 expanded variants, grouped under the 168 original VerilogEval v2.0 and RTLLM v2.0 source designs from which they were generated.
- **[eval/](eval/)** — a unified evaluation script that runs any LLM against any of the six benchmarks under iverilog (or cocotb for CVDP). LLM backend and simulator are both pluggable. See [eval/README.md](eval/README.md).

## Benchmark status

| Benchmark | Total tasks | Repaired |
|---|---:|---:|
| VerilogEval Human v1 | 156 | 14 |
| VerilogEval Human v2 | 156 | 8 |
| VerilogEval Machine v1 | 143 | 11 |
| RTLLM v2.1 | 50 | 5 |
| CVDP cid002 | 94 | 4 |
| CVDP cid003 | 77 | 5 |
| **Total** | **676** | **47** |

Each repaired record carries an `ambiguity_type` field (one of `functional`, `syntax`, `diagram`) and a `fix_description` string. See [per-case-analysis/](per-case-analysis/) for the per-case rationale and the original-vs-fixed diff.

## Version 2.0 additions

### Expanded cases

The expansion release contains the following source-organized cases:

| Source benchmark | Original designs | Expanded variants |
|---|---:|---:|
| VerilogEval v2.0 | 119 | 282 |
| RTLLM v2.0 | 49 | 156 |
| **Total** | **168** | **438** |

Each source folder contains the original description and golden RTL, followed by its variants grouped by logic-shift category. Each variant folder contains `description.txt`, `golden_rtl.sv`, and `case.json`. 

## How we evaluate

Each benchmark has its own prompt-construction convention. We provide a normalized eval script for all benchmarks:

| Benchmark | What the LLM sees | Simulator |
|---|---|---|
| VerilogEval Human v1 / Machine v1 | `detail_description + module_header` | iverilog |
| VerilogEval Human v2 | `instruction` | iverilog |
| RTLLM v2.1 | `design_prompt` | iverilog |
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
    --llm azure_gpt4o_mini --only-fixed-records --output /tmp/rtl-benchmt-v1-fixed.jsonl
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
