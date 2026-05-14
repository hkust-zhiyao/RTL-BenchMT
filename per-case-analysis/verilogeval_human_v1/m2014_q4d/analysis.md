# verilogeval_human_v1 — `m2014_q4d`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec says the flip-flop has no reset but does not state any initial value for 'out', so the canonical's initialization of 'out' to 0 is not derivable; without it, 'out' stays X forever because 'in ^ x = x'.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
; instead, 'out' has an initial value of 0 at time zero
```
