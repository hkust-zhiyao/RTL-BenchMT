# verilogeval_human_v1 — `lfsr5`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The prompt specifies taps 'at bit positions 5 and 3' without stating whether these are 1-indexed polynomial positions or 0-indexed Verilog bit indices, so a literal reader cannot deterministically map them to q[4] and q[2].

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
bit positions are numbered 1 through 5 and correspond to q[0] through q[4], so the tap at position 3 XORs into q[2] and the tap at position 5 is the feedback into q[4] from the output bit q[0]. The
```
