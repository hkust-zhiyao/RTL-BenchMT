# verilogeval_machine_v1 — `mt2015_q4b`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description self-contradicts: it labels the function as the negation of XOR (i.e., XNOR) but then describes XOR semantics ('true if either x or y is true, but not both'), so a literal reader cannot deterministically pick z = ~(x^y) over z = x^y.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 441 chars; fixed: 465 chars (ratio 1.05). See the two files for the full text.
