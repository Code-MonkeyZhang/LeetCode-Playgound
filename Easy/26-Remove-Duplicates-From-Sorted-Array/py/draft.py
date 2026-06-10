# LeetCode 26 — 删除有序数组中的重复项
#
# 题目描述：给你一个非严格递增排列的数组 nums，请你原地删除重复出现的元素，使每个元素只出现一次，
# 返回删除后数组的新长度。元素的相对顺序应该保持一致。然后返回 nums 中唯一元素的个数。
#
# 示例 1：输入: nums = [1,1,2] → 输出: 2, nums = [1,2,_]
# 示例 2：输入: nums = [0,0,1,1,1,2,2,3,3,4] → 输出: 5, nums = [0,1,2,3,4,_,_,_,_,_]

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
