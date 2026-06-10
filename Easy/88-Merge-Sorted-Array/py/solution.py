# LeetCode 88 — 合并两个有序数组
#
# 题目描述：给你两个按非递减顺序排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n，
# 分别表示 nums1 和 nums2 中的元素数目。请你合并 nums2 到 nums1 中，使合并后的数组同样按非递减顺序排列。
# 注意：最终合并后数组不应由函数返回，而是存储在数组 nums1 中。
# nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0，应忽略。nums2 的长度为 n。
#
# 示例 1：输入: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 → 输出: [1,2,2,3,5,6]
# 示例 2：输入: nums1 = [1], m = 1, nums2 = [], n = 0 → 输出: [1]
# 示例 3：输入: nums1 = [0], m = 0, nums2 = [1], n = 1 → 输出: [1]

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = len(nums1) - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
