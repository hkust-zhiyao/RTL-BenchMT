"""Template LLMCaller for users who want to plug in their own backend.

Copy this file, rename the class, and fill in `__call__`. Then register it
in `eval/evaluate.py` (search for `LLM_REGISTRY`) so the CLI can pick it up
via `--llm <your_name>`.

The contract is a single method: take (prompt, system_prompt) and return
the model's text. Anything else — batching, retries, key rotation, local
inference, OpenRouter, vLLM, llama.cpp, ollama — is your responsibility.
"""

from typing import Optional


class CustomLLM:
    """Replace this with your own backend."""

    name = "custom"

    def __init__(self, **kwargs):
        # Stash whatever config you need.
        self.config = kwargs

    def __call__(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        raise NotImplementedError(
            "Implement CustomLLM.__call__ — call your LLM and return its text "
            "response. See eval/llm/azure_gpt.py for an Azure OpenAI example."
        )
