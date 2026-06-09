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


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


assert linked_list_to_list(sol.reverseKGroup(create_linked_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
assert linked_list_to_list(sol.reverseKGroup(create_linked_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]

print("All tests passed!")
