# cvdp_cid003 — `cvdp_copilot_digital_dice_roller_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid003`

## Issue identified

The prompt names the reset port `reset_n` (active-LOW) and says `dice_value` stays at `000` while reset is asserted, but the cocotb testbench drives `dut.reset` (active-LOW) and asserts `dice_value == 1` after reset, so a literal-spec-following implementation cannot pass.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,863 chars; fixed: 2,032 chars (ratio 1.09). See the two files for the full text.
