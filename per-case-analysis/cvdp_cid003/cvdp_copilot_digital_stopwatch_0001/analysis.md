# cvdp_cid003 — `cvdp_copilot_digital_stopwatch_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid003`

## Issue identified

The spec body never names the internal 1-Hz pulse signal that the testbench probes directly (`dut.one_sec_pulse`), so a literal-spec-following LLM cannot recover the exact required identifier from the spec proper.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
The once-per-second strobe must be exposed as a module-internal signal named exactly `one_sec_pulse`, asserted high for exactly one period of `clk` once every second.
-
```
