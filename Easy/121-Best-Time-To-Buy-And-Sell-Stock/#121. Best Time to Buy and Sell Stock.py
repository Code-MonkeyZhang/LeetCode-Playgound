# LeetCode 121 — 买卖股票的最佳时机
#
# 题目描述：给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 如果你不能获取任何利润，返回 0。
#
# 示例 1：输入: prices = [7,1,5,3,6,4] → 输出: 5（在第2天买入，第5天卖出，利润=6-1=5）
# 示例 2：输入: prices = [7,6,4,3,1] → 输出: 0（在这种情况下，没有交易完成，利润为0）

# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)

        return max_profit


# Example usage:
solution = Solution()

# Test cases
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))    # Expected output: 0

# You can add more test cases here
