import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from ds_utils.single_linked_list import ListNode

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()


def create_linked_list(vals):
    if not vals:
        return None
    head = ListNode(val=vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(val=v)
        cur = cur.next
    return head


assert sol.spiralMatrix(3, 5, create_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])) == [
    [3, 0, 2, 6, 8],
    [5, 0, -1, -1, 1],
    [5, 2, 4, 9, 7],
]

assert sol.spiralMatrix(1, 4, create_linked_list([0, 1, 2])) == [[0, 1, 2, -1]]

assert sol.spiralMatrix(2, 2, create_linked_list([1, 2, 3])) == [
    [1, 2],
    [-1, 3],
]

assert sol.spiralMatrix(3, 3, create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])) == [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5],
]

print("All tests passed!")
