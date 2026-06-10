# LeetCode 104 — 二叉树的最大深度
#
# 题目描述：给定一个二叉树 root，返回其最大深度。
# 二叉树的最大深度是指从根节点到最远叶子节点的最长路径上的节点数。
#
# 示例 1：输入: root = [3,9,20,null,null,15,7] → 输出: 3
# 示例 2：输入: root = [1,null,2] → 输出: 2

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
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
