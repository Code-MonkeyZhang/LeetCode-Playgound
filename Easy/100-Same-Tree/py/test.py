import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()
TreeNode = mod.TreeNode


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


assert sol.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
assert sol.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
assert sol.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
assert sol.isSameTree(None, None) is True
assert sol.isSameTree(build_tree([1]), build_tree([1])) is True
assert sol.isSameTree(build_tree([1]), None) is False
assert sol.isSameTree(None, build_tree([1])) is False

print("All tests passed!")
