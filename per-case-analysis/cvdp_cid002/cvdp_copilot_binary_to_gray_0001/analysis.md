# cvdp_cid002 — `cvdp_copilot_binary_to_gray_0001`

- **Ambiguity type:** `syntax`
- **Source benchmark:** `cvdp_cid002`

## Issue identified

The Verilog skeleton in the prompt declares the parameter list using non-Verilog syntax `module binary_to_gray (parameter WIDTH = 6) (...)`, mixing parameters and ports inside a single port-list pair, so a literal completion of the skeleton fails to elaborate.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix inserts the following clarification into the upstream prompt; everything else is preserved verbatim.

```
#
```
