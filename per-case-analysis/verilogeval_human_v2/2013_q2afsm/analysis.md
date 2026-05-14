# verilogeval_human_v2 — `2013_q2afsm`

- **Ambiguity type:** `diagram`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The FSM state diagram lists a state D but provides no transitions out of D and no output annotation for D, while also giving the A->D transition the wrong condition (r0=0,r1=0,r2=0, identical to A->A) — leaving the LLM unable to recover the canonical r[2]-grant behavior for state D.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,997 chars; fixed: 2,063 chars (ratio 1.03). See the two files for the full text.
