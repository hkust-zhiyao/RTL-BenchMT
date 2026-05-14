"""LLMCaller protocol — every LLM backend implements this single method.

Users write a class with a `__call__(prompt, system_prompt) -> str` method
and register it via the `--llm` CLI flag. Examples in `azure_gpt.py` and
`stub.py`.
"""

from typing import Protocol, Optional


class LLMCaller(Protocol):
    name: str

    def __call__(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Return the LLM's text response. Synchronous, single completion."""
        ...
