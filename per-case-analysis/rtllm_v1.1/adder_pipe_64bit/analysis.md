# rtllm_v1.1 — `adder_pipe_64bit`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `rtllm_v1.1`

## Issue identified

The prompt does not specify that the module must declare two named parameters (DATA_WIDTH=64, STG_WIDTH=16) that the testbench binds by name during instantiation, nor does it pin down the per-stage chunk width or the number of pipeline stages.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,116 chars; fixed: 1,537 chars (ratio 1.38). See the two files for the full text.
