# verilogeval_human_v1 — `2013_q2afsm`

- **Ambiguity type:** `diagram`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The state-diagram bullet listing the A->D transition specifies r1=0,r2=0,r3=0, which is identical to the A->A self-loop condition and contradicts the canonical, which moves to D only when r[3]=1 (with r[1]=r[2]=0).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
1
```
