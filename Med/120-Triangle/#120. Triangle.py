# LeetCode 120 — 三角形最小路径和
#
# 题目描述：给定一个三角形 triangle，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的节点上。相邻节点指的是下标与当前节点下标相同或等于当前节点下标+1 的两个节点。
#
# 示例 1：输入: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] → 输出: 11（路径 2→3→5→1 的和为11）
# 示例 2：输入: triangle = [[-10]] → 输出: -10

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Your solution here
        layer = len(triangle)
        # range(start,stop,step)
        for i in range(layer-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]


def test_solution():
    sol = Solution()

    # Test case 1
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert sol.minimumTotal(
        triangle1) == 11, f"Test case 1 failed. Expected 11, got {sol.minimumTotal(triangle1)}"

    # Test case 2
    triangle2 = [[-10]]
    assert sol.minimumTotal(
        triangle2) == -10, f"Test case 2 failed. Expected -10, got {sol.minimumTotal(triangle2)}"

    # Additional test case
    triangle3 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    assert sol.minimumTotal(
        triangle3) == 14, f"Test case 3 failed. Expected 14, got {sol.minimumTotal(triangle3)}"

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_solution()
