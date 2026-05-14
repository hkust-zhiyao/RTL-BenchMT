# cvdp_cid003 — `cvdp_copilot_convolutional_encoder_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid003`

## Issue identified

The prompt does not commit to a specific internal 2-bit register named shift_reg, nor does it pin down that encoded_bit1/encoded_bit2 are combinational functions of the current data_in and the pre-update shift_reg (so the new data_in must NOT appear in shift_reg on the same cycle's outputs).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,423 chars; fixed: 2,207 chars (ratio 1.55). See the two files for the full text.
