# rtllm_v2.1 — `freq_divbyfrac`

- **Ambiguity type:** `functional`
- **Source benchmark:** `rtllm_v2.1`

## Issue identified

The spec does not pin down which clock edge each of the two intermediate clocks is registered on, nor the exact counter values at which each intermediate clock asserts, so a literal reader cannot reproduce the canonical's specific (posedge cnt==0/cnt==4) and (negedge cnt==1/cnt==4) trigger points required to match the testbench waveform.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
Specifically, the first intermediate clock is registered on the posedge of clk and is set high when cnt == 0 or cnt == (MUL2_DIV_CLK/2)+1, and low otherwise. The second intermediate clock is registered on the negedge of clk and is set high when cnt == 1 or cnt == (MUL2_DIV_CLK/2)+1, and low otherwise. Both registers reset to 0 on the active-low reset.
```

## RTLLM v2.1 synchronization

The revised prompt incorporates the applicable specification-side clarifications released upstream in RTLLM v2.1. `original.txt` is retained as the historical upstream prompt used for the paper's original-vs-fixed comparison. Testbench-only v2.1 changes are not imported into RTL-BenchMT.
