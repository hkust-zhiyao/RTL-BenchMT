"""Extract Verilog code from an LLM response.

LLMs produce code in a few common shapes — fenced markdown block, raw
`module ... endmodule`, or a mix. This module returns the most plausible
single-module Verilog body.
"""

import re


def extract_verilog(response: str) -> str:
    """Return the most plausible Verilog code in `response`.

    Strategy (ordered):
      1. Pick the longest ```verilog | ```systemverilog | ```sv | ```v block.
      2. If no fenced block, pick the largest substring that matches
         `module ... endmodule` (greedy across the whole response).
      3. Fall back to the raw response.
    """
    if not response:
        return ""

    # 1. fenced code block
    fenced = re.findall(
        r"```(?:verilog|systemverilog|sv|v)?\s*\n?(.*?)```",
        response, flags=re.DOTALL | re.IGNORECASE,
    )
    fenced = [b.strip() for b in fenced if b.strip()]
    if fenced:
        # Prefer blocks that contain `module` + `endmodule`
        modular = [b for b in fenced if "module" in b and "endmodule" in b]
        if modular:
            return max(modular, key=len)
        return max(fenced, key=len)

    # 2. raw module ... endmodule
    raw = re.findall(
        r"\bmodule\s+\w[\s\S]*?\bendmodule\b",
        response, flags=re.IGNORECASE,
    )
    if raw:
        return max(raw, key=len).strip()

    # 3. fall back
    return response.strip()
