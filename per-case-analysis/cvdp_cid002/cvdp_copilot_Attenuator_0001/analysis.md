# cvdp_cid002 — `cvdp_copilot_Attenuator_0001`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `cvdp_cid002`

## Issue identified

The prose labels `reset` as a synchronous reset, but the partial-code template forces an asynchronous reset sensitivity list (`always @(posedge clk or posedge reset)`), so a literal-spec-following LLM cannot tell whether the intended reset semantics are synchronous (per the signal table) or asynchronous (per the template).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
Active-high asynchronous reset signal.
```
