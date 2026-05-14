# verilogeval_human_v1 — `ece241_2014_q5b`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The prompt mandates one-hot state encoding, but the canonical solution uses a single 1-bit binary state register with parameters A=0 and B=1, leaving the spec internally inconsistent on how the two states must be encoded.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
a 1-bit binary state encoding with A=0 and B=1
```
