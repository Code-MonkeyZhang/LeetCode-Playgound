import importlib.util
from pathlib import Path
from collections import deque

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()
TreeNode = mod.TreeNode


def build_tree(values):
    if not values:
        return None
    root = TreeNode(val=values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(val=values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(val=values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


assert tree_to_list(sol.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
assert tree_to_list(sol.invertTree(build_tree([2, 1, 3]))) == [2, 3, 1]
assert tree_to_list(sol.invertTree(build_tree([]))) == []

print("All tests passed!")
