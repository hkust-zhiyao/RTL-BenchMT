# cvdp_cid003 — `cvdp_copilot_fsm_seq_detector_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid003`

## Issue identified

The prompt does not pin down the FSM state semantics for an 8-bit pattern with eight states (S0-S7) nor the exact post-detection state on overlap, so a literal reader cannot determine when seq_detected fires relative to the 8th bit or which state the FSM returns to after a match.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 2,874 chars; fixed: 3,509 chars (ratio 1.22). See the two files for the full text.
