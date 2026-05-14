"""Simulator protocol — pluggable evaluation backend."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol


@dataclass
class SimResult:
    passed: bool
    output: str = ""
    error: Optional[str] = None
    duration_s: float = 0.0
    stage: str = ""  # "compile" | "run" | ""


class Simulator(Protocol):
    name: str

    def run(self, dut_code: str, record: dict, work_dir: Path,
            bench: str) -> SimResult:
        """Compile + run the DUT against the record's testbench. Return
        SimResult with `passed` set."""
        ...
