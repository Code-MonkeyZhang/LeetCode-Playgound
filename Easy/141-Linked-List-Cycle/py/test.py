import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ds_utils.single_linked_list import ListNode


filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"
spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()


def build_cycle_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(val=v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


assert sol.hasCycle(build_cycle_list([3, 2, 0, -4], 1))
assert sol.hasCycle(build_cycle_list([1, 2], 0))
assert not sol.hasCycle(build_cycle_list([1], -1))

print("All tests passed!")
