# verilogeval_machine_v1 — `dff8`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The description splits 'stored in the register' from 'output on the data output' and never pins down that q is the flip-flop's own state register, so a literal reader cannot tell whether q must update only on the rising clock edge (registered, non-transparent) or may track d combinationally between edges.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,034 chars; fixed: 1,046 chars (ratio 1.01). See the two files for the full text.
