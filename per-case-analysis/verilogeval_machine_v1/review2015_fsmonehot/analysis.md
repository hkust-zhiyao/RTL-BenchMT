# verilogeval_machine_v1 — `review2015_fsmonehot`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The spec lists ten one-hot states by name but never says which bit of the 10-bit `state` input corresponds to which named state, so the LLM cannot index `state[...]` consistently with the testbench's reference module.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The 10-bit one-hot input state encodes these states at bit positions state[0]=S, state[1]=S1, state[2]=S11, state[3]=S110, state[4]=B0, state[5]=B1, state[6]=B2, state[7]=B3, state[8]=Count and state[9]=Wait.
```
