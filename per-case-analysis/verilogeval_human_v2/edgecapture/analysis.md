# verilogeval_human_v2 — `edgecapture`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The spec does not specify which register the synchronous reset clears: the captured-output register only, or all internal state including the previous-input tracking register used for edge detection.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 567 chars; fixed: 762 chars (ratio 1.34). See the two files for the full text.
