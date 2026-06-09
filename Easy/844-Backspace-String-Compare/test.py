import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.backspaceCompare("ab#c", "ad#c")
assert sol.backspaceCompare("ab##", "c#d#")
assert not sol.backspaceCompare("a#c", "b")

print("All tests passed!")
