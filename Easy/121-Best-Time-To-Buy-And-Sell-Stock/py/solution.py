# LeetCode 121 — 买卖股票的最佳时机
#
# 题目描述：给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 如果你不能获取任何利润，返回 0。
#
# 示例 1：输入: prices = [7,1,5,3,6,4] → 输出: 5（在第2天买入，第5天卖出，利润=6-1=5）
# 示例 2：输入: prices = [7,6,4,3,1] → 输出: 0（在这种情况下，没有交易完成，利润为0）

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
