# LeetCode 122 — 买卖股票的最佳时机 II
#
# 题目描述：给你一个整数数组 prices，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。
# 你也可以先购买，然后在同一天出售。返回你能获得的最大利润。
#
# 示例 1：输入: prices = [7,1,5,3,6,4] → 输出: 7（第2天买入第3天卖出利润=4，第4天买入第5天卖出利润=3，总利润=7）
# 示例 2：输入: prices = [1,2,3,4,5] → 输出: 4（第1天买入第5天卖出，总利润=4）
# 示例 3：输入: prices = [7,6,4,3,1] → 输出: 0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
