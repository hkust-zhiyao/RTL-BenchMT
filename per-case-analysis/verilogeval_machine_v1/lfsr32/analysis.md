# verilogeval_machine_v1 — `lfsr32`

- **Ambiguity type:** `functional`
- **Source benchmark:** `verilogeval_machine_v1`

## Issue identified

The detail_description's tap-XOR description is incoherent: it says bits 21, 1, and 0 are 'XORed with the value of bit 0', but for bit 0 this self-XOR collapses to zero, while the canonical instead applies the taps to the post-shift positions (so q_next[0] = q[1] ^ q[0], not q[0] ^ q[0]).

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 1,028 chars; fixed: 1,018 chars (ratio 0.99). See the two files for the full text.
