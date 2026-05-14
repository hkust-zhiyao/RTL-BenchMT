# verilogeval_human_v1 — `review2015_fsmonehot`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec does not tell the reader to derive each next-state/output equation as a disjunction of individual one-hot bits of `state` (e.g., `state[B2]`) rather than as equality comparisons against full 10-bit constants, so a literal reader may produce code that matches the canonical only on one-hot inputs and diverges under the random-input phase the testbench applies.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
Each next-state and output equation must be written as a function of the individual bits of the `state` input (one bit per state, indexed by its position in the one-hot encoding above), not as equality comparisons against 10-bit one-hot constants.
```
