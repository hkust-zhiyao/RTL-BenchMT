# verilogeval_human_v1 — `kmap4`

- **Ambiguity type:** `diagram`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The K-map header rows and columns are labeled `ab` and `cd` with Gray-coded values `00 01 11 10`, but the spec never states the bit ordering within those two-bit labels (i.e., that `a` and `c` are the MSBs of their respective axes), so a literal reader cannot deterministically map a cell to a minterm of `{a,b,c,d}`.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
In the axis labels, `a` and `c` are the most-significant bits.
```
