# rtllm_v2.1 — `serial2parallel`

- **Ambiguity type:** `functional`
- **Source benchmark:** `rtllm_v2.1`

## Issue identified

The prompt does not specify the exact cycle on which dout_parallel/dout_valid become valid relative to the 8th serial bit, nor that the 4-bit counter must count from 0 up to 8 (nine states) and reset to 0 whenever din_valid is deasserted.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,370 chars; fixed: 1,615 chars (ratio 1.18). See the two files for the full text.

## RTLLM v2.1 synchronization

The revised prompt incorporates the applicable specification-side clarifications released upstream in RTLLM v2.1. `original.txt` is retained as the historical upstream prompt used for the paper's original-vs-fixed comparison. Testbench-only v2.1 changes are not imported into RTL-BenchMT.
