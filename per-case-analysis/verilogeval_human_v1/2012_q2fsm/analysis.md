# verilogeval_human_v1 — `2012_q2fsm`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The prompt never states what the parenthesized number next to each state name means, so the rule that drives the output z (z = 1 in states E and F, else 0) is not derivable from the spec.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The number in parentheses next to each state name is the value of output z while the FSM is in that state.

//
```
