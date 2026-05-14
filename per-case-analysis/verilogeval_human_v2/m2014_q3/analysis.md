# verilogeval_human_v2 — `m2014_q3`

- **Ambiguity type:** `diagram`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The K-map labels its inputs x[1], x[2], x[3], x[4] (1-based), but the module port is declared as 'input x (4 bits)' which a literal reader will model as 'input [3:0] x' (0-based, x[3]=MSB), leaving the correspondence between K-map indices 1..4 and canonical bit positions 3..0 undefined.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 519 chars; fixed: 707 chars (ratio 1.36). See the two files for the full text.
