# verilogeval_machine_v1 — `edgecapture`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The spec says reset clears out 'initially', leaving unclear whether reset is one-shot or re-asserted on every clock cycle that reset is high; the canonical re-clears out on every posedge clk while reset is asserted (synchronous reset that overrides the OR-update).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 865 chars; fixed: 840 chars (ratio 0.97). See the two files for the full text.
