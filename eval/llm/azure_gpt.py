"""Example LLMCaller: HKUST Azure OpenAI endpoint (GPT-4o, GPT-4o-mini, ...).

API key is read from `eval/config/openai-api-list.txt` (one key per line —
the first non-comment line is used). Override with the
`AZURE_OPENAI_API_KEY` environment variable.

Usage:
    from eval.llm.azure_gpt import AzureGPT
    caller = AzureGPT(model="gpt-4o-mini")
    response = caller("Write a 4-bit counter.", system_prompt="You are...")
"""

import os
from pathlib import Path
from typing import Optional


_DEFAULT_ENDPOINT = "https://hkust.azure-api.net/"
_DEFAULT_API_VERSION = "2024-10-21"
_KEY_FILE = Path(__file__).resolve().parents[1] / "config" / "openai-api-list.txt"


def _load_api_key() -> str:
    if (k := os.environ.get("AZURE_OPENAI_API_KEY")):
        return k
    if not _KEY_FILE.exists():
        raise RuntimeError(
            f"No API key found. Set AZURE_OPENAI_API_KEY or create "
            f"{_KEY_FILE} with one key per line."
        )
    for line in _KEY_FILE.read_text().splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s
    raise RuntimeError(f"{_KEY_FILE} contains no usable key")


class AzureGPT:
    """LLMCaller backed by HKUST's Azure OpenAI proxy."""

    name = "azure_gpt"

    def __init__(self, model: str = "gpt-4o-mini",
                 endpoint: str = _DEFAULT_ENDPOINT,
                 api_version: str = _DEFAULT_API_VERSION,
                 temperature: float = 0.0,
                 max_tokens: int = 2048,
                 timeout: int = 120):
        try:
            from openai.lib.azure import AzureOpenAI
        except ImportError as e:
            raise RuntimeError(
                "Install the openai package: pip install openai"
            ) from e
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.name = f"azure_{model.replace('/', '_')}"
        self._client = AzureOpenAI(
            azure_endpoint=endpoint.rstrip("/"),
            azure_deployment=model,
            api_version=api_version,
            api_key=_load_api_key(),
        )

    def __call__(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
        )
        return (resp.choices[0].message.content or "").strip()
