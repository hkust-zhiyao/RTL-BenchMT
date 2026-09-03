# rtllm_v2.1 — `parallel2serial`

- **Ambiguity type:** `functional`
- **Source benchmark:** `rtllm_v2.1`

## Issue identified

The spec does not commit valid_out to a single-cycle pulse coincident with the MSB output, leaving open the natural reading that valid_out stays high for all four serial-output cycles.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
valid_out is high for exactly one cycle per 4-bit group, asserted on the same cycle that the MSB appears on dout, and is low during the next three cycles while the remaining three bits are emitted.
```
