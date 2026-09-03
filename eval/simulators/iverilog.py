"""iverilog-based Simulator for VerilogEval (V1, V2, Machine v1) and RTLLM.

Compilation: iverilog -g2012 -o sim dut.sv tb.v
Run:         vvp sim

Pass/fail parsing handles the conventions used by each upstream:

  VerilogEval Human v1, v2, Machine v1
    The testbench prints `Mismatches: <n> in <total> samples` and finishes.
    Pass iff n == 0 (and at least one sample compared).

  RTLLM v2.1
    The testbench prints either `===========Your Design Passed===========` /
    `Final mismatch ... ` / `Test passed` style strings — we use a small
    set of regexes biased toward the canonical formats.

iverilog is required on PATH. cocotb is NOT used here — see
`cocotb_iverilog.py` for CVDP.
"""

import re
import shutil
import subprocess
import time
from pathlib import Path

from .base import SimResult


class IverilogSimulator:
    name = "iverilog"

    def __init__(self, compile_timeout: int = 60, run_timeout: int = 60):
        if not shutil.which("iverilog"):
            raise RuntimeError("iverilog not found on PATH. apt-get install iverilog")
        if not shutil.which("vvp"):
            raise RuntimeError("vvp not found on PATH (ships with iverilog)")
        self.compile_timeout = compile_timeout
        self.run_timeout = run_timeout

    def run(self, dut_code: str, record: dict, work_dir: Path, bench: str) -> SimResult:
        if bench.startswith("cvdp_"):
            return SimResult(
                passed=False,
                error=f"iverilog simulator does not handle {bench} — use cocotb_iverilog",
                stage="dispatch",
            )

        work_dir.mkdir(parents=True, exist_ok=True)
        dut_path = work_dir / "dut.sv"
        tb_path = work_dir / "tb.v"
        sim_bin = work_dir / "sim"

        dut_path.write_text(dut_code)

        if bench == "rtllm_v2.1":
            tb_text = record.get("testbench", "")
        else:
            tb_text = record.get("test", "")
        if not tb_text:
            return SimResult(passed=False, error="no testbench in record", stage="setup")
        tb_path.write_text(tb_text)

        # VerilogEval Human v2 testbenches reference an external `RefModule`
        # (the golden) — it ships in record["reference"]. V1 and Machine v1
        # inline the reference inside `test`, so this path is V2-only.
        compile_inputs = [str(dut_path), str(tb_path)]
        ref_path = work_dir / "ref.sv"
        if bench == "verilogeval_human_v2" and record.get("reference"):
            ref_path.write_text(record["reference"])
            compile_inputs.append(str(ref_path))

        # ── compile ──────────────────────────────────────────────────────
        t0 = time.time()
        try:
            cp = subprocess.run(
                ["iverilog", "-g2012", "-o", str(sim_bin), *compile_inputs],
                capture_output=True, text=True, timeout=self.compile_timeout,
            )
        except subprocess.TimeoutExpired:
            return SimResult(passed=False, error="iverilog compile timeout",
                             stage="compile", duration_s=time.time() - t0)
        if cp.returncode != 0:
            return SimResult(passed=False, output=cp.stdout, error=cp.stderr,
                             stage="compile", duration_s=time.time() - t0)

        # ── run ──────────────────────────────────────────────────────────
        try:
            rp = subprocess.run(
                ["vvp", str(sim_bin)],
                capture_output=True, text=True, timeout=self.run_timeout,
            )
        except subprocess.TimeoutExpired:
            return SimResult(passed=False, error="vvp run timeout",
                             stage="run", duration_s=time.time() - t0)

        out = rp.stdout
        passed = _judge(bench, out)
        return SimResult(
            passed=passed,
            output=out,
            error=rp.stderr if rp.stderr else None,
            stage="run",
            duration_s=time.time() - t0,
        )


# ── pass/fail judgement ──────────────────────────────────────────────────

_VE_MISMATCHES = re.compile(r"Mismatches:\s*(\d+)\s+in\s+(\d+)\s+samples", re.IGNORECASE)


def _judge(bench: str, output: str) -> bool:
    if bench.startswith("verilogeval_"):
        m = _VE_MISMATCHES.search(output)
        if not m:
            # Some VerilogEval testbenches use `Hint:` only on failure or
            # `OK`/`INCORRECT` markers via $finish codes. Fall back.
            if re.search(r"\bINCORRECT\b", output):
                return False
            if re.search(r"\bOK\b", output):
                return True
            return False
        n_mis, n_total = int(m.group(1)), int(m.group(2))
        return n_mis == 0 and n_total > 0

    if bench == "rtllm_v2.1":
        # RTLLM's testbenches print a small number of conventional markers.
        # We require an explicit pass marker AND no "fail/error" marker.
        out_lower = output.lower()
        fail_signals = (
            "your design failed", "final mismatch", "test failed",
            "fail!", "error!", "mismatch!",
        )
        pass_signals = (
            "your design passed", "test passed", "pass!", "all tests passed",
        )
        if any(s in out_lower for s in fail_signals):
            return False
        if any(s in out_lower for s in pass_signals):
            return True
        # Fall back: count `error = 0` style lines that some testbenches use.
        if re.search(r"error\s*=\s*0\b", out_lower) and "error" in out_lower:
            return True
        return False

    return False
