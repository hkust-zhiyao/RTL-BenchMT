# verilogeval_machine_v1 — `rotate100`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description swaps the rotation directions: it states ena==2'h1 left-shifts and ena==2'h2 right-shifts, but the canonical does the opposite, so a literal reader writes the wrong direction for both ena codes.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,416 chars; fixed: 1,518 chars (ratio 1.07). See the two files for the full text.
