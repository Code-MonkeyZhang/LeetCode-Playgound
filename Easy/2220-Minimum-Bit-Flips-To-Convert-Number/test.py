import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.minBitFlips(10, 7) == 3
assert sol.minBitFlips(3, 4) == 3

print("All tests passed!")
