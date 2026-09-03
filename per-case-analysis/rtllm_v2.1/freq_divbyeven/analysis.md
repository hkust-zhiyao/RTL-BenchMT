# rtllm_v2.1 — `freq_divbyeven`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `rtllm_v2.1`

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

## RTLLM v2.1 synchronization

The revised prompt incorporates the applicable specification-side clarifications released upstream in RTLLM v2.1. `original.txt` is retained as the historical upstream prompt used for the paper's original-vs-fixed comparison. Testbench-only v2.1 changes are not imported into RTL-BenchMT.
