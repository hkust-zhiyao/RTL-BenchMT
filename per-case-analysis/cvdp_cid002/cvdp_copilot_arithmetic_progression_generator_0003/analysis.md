# cvdp_cid002 — `cvdp_copilot_arithmetic_progression_generator_0003`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid002`

## Issue identified

The prompt asks the candidate to compute the local parameter WIDTH_OUT_VAL 'to avoid overflow' but never specifies the formula the testbench checks; the canonical/expected value is clog2(SEQUENCE_LENGTH) + DATA_WIDTH, which is not derivable from the prose.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
local parameter WIDTH_OUT_VAL must be set to `$clog2(SEQUENCE_LENGTH) + DATA_WIDTH` so that out_val can hold the worst-case accumulated sum (start_val plus up to SEQUENCE_LENGTH-1 step_size additions) without overflow. The
```
