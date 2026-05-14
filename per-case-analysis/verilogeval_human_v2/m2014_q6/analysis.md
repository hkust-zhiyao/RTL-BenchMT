# verilogeval_human_v2 — `m2014_q6`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v2`

## Issue identified

The prompt does not specify the reset behavior: whether reset is synchronous or asynchronous, and which state the FSM enters on reset.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The reset input is synchronous and active high; when it is asserted at a positive clock edge, the state machine returns to state A.
```
