# verilogeval_machine_v1 — `m2014_q4d`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description contradicts itself about when out toggles: the body says out = in XOR out (so toggling depends on in), but the closing sentence claims out toggles on every rising clock edge regardless of in.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 576 chars; fixed: 594 chars (ratio 1.03). See the two files for the full text.
