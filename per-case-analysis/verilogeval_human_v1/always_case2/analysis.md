# verilogeval_human_v1 — `always_case2`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec says 'first 1 bit in the vector' without naming the scan direction; the example implies LSB-first but a literal reader scanning the printed bit-string left-to-right would pick MSB-first and produce the wrong position.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
, scanning from the least-significant bit upward
```
