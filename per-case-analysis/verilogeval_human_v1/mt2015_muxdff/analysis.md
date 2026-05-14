# verilogeval_human_v1 — `mt2015_muxdff`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_human_v1`

## Issue identified

The prompt does not specify the mux select polarity of the submodule (which input feeds the flip-flop when L=1 vs L=0), nor the mapping between the submodule's r_in/q_in ports and the full_module behavior.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
On each posedge clk the flip-flop output Q loads r_in when L is 1 and loads q_in when L is 0, matching the full_module behavior. Q is initialized to 0.
```
