import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
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


assert sol.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
assert sol.maxDepth(build_tree([1])) == 1
assert sol.maxDepth(build_tree([])) == 0
assert sol.maxDepth(build_tree([1, None, 2])) == 2
assert sol.maxDepth(build_tree([1, 2, 3, 4])) == 3

print("All tests passed!")
