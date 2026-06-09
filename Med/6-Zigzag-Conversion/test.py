import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert sol.convert("A", 1) == "A"

print("All tests passed!")
