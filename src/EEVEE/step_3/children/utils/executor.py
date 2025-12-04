"""Code execution sandbox - runs Python code in isolated subprocess with timeout."""
import asyncio
import json
import os
import sys
import tempfile
import textwrap
from typing import Optional, List


async def run_code(code: str, input_grid: list[list[int]], timeout_s: float = 5.0) -> tuple[bool, str]:
    """
    Run user code in a subprocess asynchronously.
    
    Args:
        code: Python code containing arc_transform function
        input_grid: 2D list of integers
        timeout_s: Timeout in seconds
    
    Returns:
        (ok, result_or_error) - ok is True if execution succeeded
    """
    script = _create_execution_script(code)
    
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "solver_exec.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write(textwrap.dedent(script))
        
        proc = await asyncio.create_subprocess_exec(
            sys.executable,
            path,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=td,
            env={"PYTHONHASHSEED": "0"},
        )
        
        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(input=json.dumps({"input": input_grid}).encode()),
                timeout=timeout_s,
            )
        except asyncio.TimeoutError:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            return False, "timeout"
        
        if proc.returncode != 0:
            return False, (stderr.decode() or stdout.decode()).strip()
        
        try:
            payload = json.loads(stdout.decode())
            return bool(payload.get("ok")), json.dumps(payload.get("result"))
        except (json.JSONDecodeError, ValueError) as e:
            return False, f"bad-json: {e}"


def _create_execution_script(code: str) -> str:
    """Build the sandbox script that executes the arc_transform function."""
    return f"""
{code}

if __name__ == '__main__':
    import json
    import numpy as np
    import scipy
    from sys import stdin
    data = json.load(stdin)
    output_grid = arc_transform(np.array(data['input']))
    print(json.dumps({{"ok": True, 'result': output_grid.tolist()}}))
"""


def execute_on_single_input_sync(code: str, input_grid: List[List[int]]) -> Optional[List[List[int]]]:
    """Synchronous wrapper - executes code on a single input and returns output grid or None."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        ok, result_str = loop.run_until_complete(run_code(code, input_grid, timeout_s=5.0))
        if not ok:
            return None
        
        try:
            return json.loads(result_str)
        except (json.JSONDecodeError, ValueError):
            return None
    finally:
        loop.close()
