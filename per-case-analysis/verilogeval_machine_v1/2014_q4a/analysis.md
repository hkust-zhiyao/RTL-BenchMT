# verilogeval_machine_v1 — `2014_q4a`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The prose describes R contradictorily as both an asynchronous reset that forces Q low and as the data input selected when L is high; the canonical uses R only as a data input with no reset behavior.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,329 chars; fixed: 1,300 chars (ratio 0.98). See the two files for the full text.
