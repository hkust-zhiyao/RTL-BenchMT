# verilogeval_human_v1 — `lfsr32`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec does not pin down the shift direction or which bit serves as the 'output bit' that drives the XOR feedback, so a literal reader cannot derive that the LFSR shifts toward the LSB and uses q[0] as the feedback bit.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The register shifts toward the least significant bit, and bit 1 is the output bit that feeds back into position 32 and is XORed into the other tapped positions.
```
