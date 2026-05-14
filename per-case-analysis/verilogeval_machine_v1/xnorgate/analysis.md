# verilogeval_machine_v1 — `xnorgate`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description self-contradicts: it labels the function as the logical negation of XOR (which is XNOR, true when a==b) but then describes the truth table as 'true when the inputs are not equal' (which is XOR, true when a!=b).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 510 chars; fixed: 510 chars (ratio 1.00). See the two files for the full text.
