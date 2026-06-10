# LeetCode 100 — 相同的树
#
# 题目描述：给你两棵二叉树的根节点 p 和 q，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1：输入: p = [1,2,3], q = [1,2,3] → 输出: true
# 示例 2：输入: p = [1,2], q = [1,null,2] → 输出: false
# 示例 3：输入: p = [1,2,1], q = [1,1,2] → 输出: false

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
        if p is None or q is None:
            if p == q:
                return True
            else:
                return False

        if p.val != q.val:
            return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isRightSame

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
