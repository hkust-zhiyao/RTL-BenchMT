"""Build the LLM-visible spec for one benchmark record.

Each benchmark has a different layout. This module is the SINGLE source of
truth for "what does the LLM see for this task". It returns a (system,
user) tuple that is passed to LLMCaller.
"""

DEFAULT_SYSTEM = (
    "You are a professional Verilog designer. Given a specification, "
    "produce a complete, synthesizable Verilog module that implements it. "
    "Wrap your final code in a single ```verilog ... ``` block. Do not "
    "include a testbench, do not add explanatory prose outside the code "
    "block, and preserve the exact module and port names asked for."
)


def build_prompt(bench, record, variant="fixed"):
    """Return (system_prompt, user_prompt) for the given record.

    `variant`: "fixed" (use the agentic-pipeline-revised spec, present only
    when ambiguity_fixed=True) or "original" (use the upstream spec).
    """
    if bench in ("verilogeval_human_v1", "verilogeval_machine_v1"):
        if variant == "fixed":
            spec = record.get("detail_description", "")
        else:
            spec = (record.get("original_detail_description", "")
                    or record.get("detail_description", ""))
        header = record.get("prompt", "")
        user = (spec.rstrip() + "\n\n" + header.lstrip()) if spec else header
        return DEFAULT_SYSTEM, user

    if bench == "verilogeval_human_v2":
        if variant == "fixed":
            user = record.get("instruction", "") or record.get("prompt", "")
        else:
            user = (record.get("original_prompt", "")
                    or record.get("instruction", "")
                    or record.get("prompt", ""))
        return DEFAULT_SYSTEM, user

    if bench == "rtllm_v1.1":
        if variant == "fixed":
            user = record.get("design_prompt", "")
        else:
            user = (record.get("original_design_prompt", "")
                    or record.get("design_prompt", ""))
        return DEFAULT_SYSTEM, user

    if bench.startswith("cvdp_"):
        inp = record["input"]
        if variant == "fixed":
            user = inp.get("prompt", "")
        else:
            user = inp.get("original_prompt", "") or inp.get("prompt", "")
        return DEFAULT_SYSTEM, user

    raise ValueError(f"unknown benchmark: {bench}")


def has_variant(record, variant):
    """Return True if the record carries the requested variant.

    A `fixed` variant is only present on records with ambiguity_fixed=True.
    A record always has an `original` variant.
    """
    if variant == "fixed":
        return bool(record.get("ambiguity_fixed", False))
    return True
