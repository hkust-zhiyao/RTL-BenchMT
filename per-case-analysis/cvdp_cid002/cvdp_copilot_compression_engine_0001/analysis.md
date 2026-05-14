# cvdp_cid002 — `cvdp_copilot_compression_engine_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid002`

## Issue identified

The prose definition of `exponent_o` (zero-based index of the first set bit from MSB) contradicts the example table and the testbench, which encode the exponent as the highest set-bit position within `num_i[23:12]` minus 11 (so 0 when no bit above bit 11 is set, 12 when bit 23 is set).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 7,641 chars; fixed: 8,165 chars (ratio 1.07). See the two files for the full text.
