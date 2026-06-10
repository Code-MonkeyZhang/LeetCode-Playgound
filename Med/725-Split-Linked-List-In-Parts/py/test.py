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


def parts_to_lists(parts):
    return [linked_list_to_list(p) for p in parts]


assert parts_to_lists(sol.splitListToParts(create_linked_list([1, 2, 3]), 5)) == [[1], [2], [3], [], []]
assert parts_to_lists(sol.splitListToParts(create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

print("All tests passed!")
