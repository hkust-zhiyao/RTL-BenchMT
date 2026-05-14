# verilogeval_human_v1 — `edgecapture`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec does not pin down when out[i] becomes 1 relative to the 1->0 transition on in[i], leaving the cycle of assertion (same cycle as in's drop vs. the cycle after) under-specified.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
out[i] becomes 1 on the clock edge after the 1-to-0 transition.
```
