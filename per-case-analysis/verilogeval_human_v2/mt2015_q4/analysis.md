# verilogeval_human_v2 — `mt2015_q4`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The prompt never states the top-level module's name, but the testbench instantiates it as `TopModule top_module1`, so any other name causes elaboration failure.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
named TopModule
```
