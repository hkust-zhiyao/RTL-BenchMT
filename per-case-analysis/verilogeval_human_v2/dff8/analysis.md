# verilogeval_human_v2 — `dff8`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The prompt does not specify the power-on / pre-first-edge value of q, but the canonical and the testbench both rely on q being 0 before the first positive clock edge.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The flip-flops are initialized to 8'h0 at
time 0.
```
