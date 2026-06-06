# LeetCode 226 — 翻转二叉树
#
# 题目描述：给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。
#
# 示例 1：输入: root = [4,2,7,1,3,6,9] → 输出: [4,7,2,9,6,3,1]
# 示例 2：输入: root = [2,1,3] → 输出: [2,3,1]
# 示例 3：输入: root = [] → 输出: []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # TODO: Implement your solution here
        # Hint: Think about swapping left and right nodes recursively
        
        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Test cases helper functions
def build_tree(nodes):
    """Build a tree from a list representation [root, left, right, ...]"""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        # Add left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

def tree_to_list(root):
    """Convert a tree to a list representation for comparison"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
def run_tests():
    solution = Solution()
    
    # Test case 1: [4,2,7,1,3,6,9]
    root1 = build_tree([4,2,7,1,3,6,9])
    expected1 = [4,7,2,9,6,3,1]
    inverted1 = solution.invertTree(root1)
    result1 = tree_to_list(inverted1)
    print(f"Test case 1: {'PASS' if result1 == expected1 else 'FAIL'}")
    print(f"Expected: {expected1}")
    print(f"Got:      {result1}")
    
    # Test case 2: [2,1,3]
    root2 = build_tree([2,1,3])
    expected2 = [2,3,1]
    inverted2 = solution.invertTree(root2)
    result2 = tree_to_list(inverted2)
    print(f"Test case 2: {'PASS' if result2 == expected2 else 'FAIL'}")
    print(f"Expected: {expected2}")
    print(f"Got:      {result2}")
    
    # Test case 3: []
    root3 = build_tree([])
    expected3 = []
    inverted3 = solution.invertTree(root3)
    result3 = tree_to_list(inverted3)
    print(f"Test case 3: {'PASS' if result3 == expected3 else 'FAIL'}")
    print(f"Expected: {expected3}")
    print(f"Got:      {result3}")
    
    # Test case 4: A tree with one node [5]
    root4 = build_tree([5])
    expected4 = [5]
    inverted4 = solution.invertTree(root4)
    result4 = tree_to_list(inverted4)
    print(f"Test case 4: {'PASS' if result4 == expected4 else 'FAIL'}")
    print(f"Expected: {expected4}")
    print(f"Got:      {result4}")

# Uncomment to run tests
run_tests()
