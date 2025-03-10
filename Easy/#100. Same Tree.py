# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Your solution code goes here
        if p is None or q is None:
            if p == q:
                return True
            else:
                return False
        
        if p.val != q.val:
            return False
        
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame & isRightSame


# Test cases from the problem description
def build_tree(arr):
    """Helper function to build a tree from an array representation"""
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test Case 1
p1 = build_tree([1, 2, 3])
q1 = build_tree([1, 2, 3])
# Expected output: true

# Test Case 2
p2 = build_tree([1, 2])
q2 = build_tree([1, None, 2])
# Expected output: false

# Test Case 3
p3 = build_tree([1, 2, 1])
q3 = build_tree([1, 1, 2])
# Expected output: false

# Run tests
solution = Solution()

print("Test Case 1:", solution.isSameTree(p1, q1))  # Should be True
print("Test Case 2:", solution.isSameTree(p2, q2))  # Should be False
print("Test Case 3:", solution.isSameTree(p3, q3))  # Should be False

# You can add more custom test cases here