# verilogeval_human_v2 — `m2014_q4d`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The prompt says the flip-flop has no reset but never specifies its initial (power-on) value, leaving the XOR-feedback loop to start from X and propagate X forever in simulation.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 454 chars; fixed: 549 chars (ratio 1.21). See the two files for the full text.
