# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        思路: 如果我在中间的步骤,怎么表示现在的深度?
        现在的深度 = 右边 左边最大深度 + 1
        """

        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth,right_depth) + 1
        




# 手动构造二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 运行测试
sol = Solution()
print(sol.maxDepth(root))  # 期望输出: 3
