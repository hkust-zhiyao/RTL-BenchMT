# verilogeval_human_v2 — `review2015_fsmonehot`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The prompt specifies the one-hot state encoding using an ellipsis ('10'b0000000001, 10'b0000000010, 10'b0000000100, ... , 10'b1000000000') without explicitly stating that the i-th name in the listed tuple corresponds to state bit[i], leaving the bit-position-to-state mapping for the middle states (S110, B0, B1, B2, B3, Count) under-specified.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 2,267 chars; fixed: 2,283 chars (ratio 1.01). See the two files for the full text.
