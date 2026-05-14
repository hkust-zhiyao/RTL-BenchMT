# rtllm_v1.1 — `freq_divbyeven`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `rtllm_v1.1`

## Issue identified

The prompt declares the module name as `freq_diveven`, but the canonical solution and testbench both use `freq_divbyeven`, so a literal-spec-following LLM produces a module name that the testbench cannot instantiate.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
by
```
