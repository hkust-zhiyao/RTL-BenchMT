# verilogeval_human_v1 — `kmap3`

- **Ambiguity type:** `diagram`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The K-map's row/column labels (`cd` and `ab`) do not specify which letter is the most-significant bit, so a literal reader cannot deterministically map a label like `cd=01` to specific values of c and d.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
In the row and column labels, the leftmost letter is the most-significant bit.
```
