# verilogeval_machine_v1 — `lfsr5`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description says `q_next is assigned with q[4:1], which is the value of q except the LSB bit`, but q_next is 5 bits while q[4:1] is only 4 bits, so a literal reader cannot determine which bit positions of q_next receive q[4:1] or what happens to the remaining bit of q_next.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
[3:0]
```
