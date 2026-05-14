# verilogeval_human_v1 — `dff8`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec does not say what value q must hold before the first positive clock edge, but the canonical (and the testbench reference) initialize q to 8'h0, and the testbench samples q on both posedge and negedge starting from time 0.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
, each powering up to zero
```
