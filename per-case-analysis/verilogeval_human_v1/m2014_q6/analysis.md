# verilogeval_human_v1 — `m2014_q6`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The spec lists each state with a parenthesized number (e.g., 'A (0)', 'E (1)') but never tells the reader that this number is the Moore output value of z for that state, and it does not state the reset state.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The number in parentheses is the value of Moore output z in that state. Reset is synchronous to state A.

//
```
