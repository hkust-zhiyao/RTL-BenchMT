# cvdp_cid003 — `cvdp_copilot_axi_stream_upscale_0001`

- **Ambiguity type:** `functional`
- **Source benchmark:** `cvdp_cid003`

## Issue identified

The prompt's prose for `dfmt_type` and `dfmt_se` does not pin down the exact bit assignments for `m_axis_data[31:24]` and `m_axis_data[23]` for each combination of `dfmt_type` and `dfmt_se` (with `dfmt_enable=1`), and the existing `// CLARIFICATION:` header is forbidden meta-commentary that itself contradicts the testbench on `s_axis_ready`.

## Files in this folder

- `original.txt` — prompt as published in the upstream benchmark, in the natural reading order the LLM sees.
- `fixed.txt` — prompt after RTLBench-MT applies the targeted clarification.

## What changed

The fix rewrites the prompt rather than inserting a single block. Original: 2,642 chars; fixed: 3,173 chars (ratio 1.20). See the two files for the full text.
