# LeetCode 27 — 移除元素
#
# 题目描述：给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素。
# 元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
#
# 示例 1：输入: nums = [3,2,2,3], val = 3 → 输出: 2, nums = [2,2,_,_]
# 示例 2：输入: nums = [0,1,2,2,3,0,4,2], val = 2 → 输出: 5, nums = [0,1,4,0,3,_,_,_]

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
