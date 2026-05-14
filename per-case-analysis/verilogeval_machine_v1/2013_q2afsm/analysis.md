# verilogeval_machine_v1 — `2013_q2afsm`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

When the FSM is in state A and multiple bits of r are simultaneously high, the description does not specify which transition wins, but the canonical commits to a strict r[1] > r[2] > r[3] priority via an if/else-if chain.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,615 chars; fixed: 1,675 chars (ratio 1.04). See the two files for the full text.
