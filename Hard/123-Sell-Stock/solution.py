# LeetCode 123 — 买卖股票的最佳时机 III
#
# 题目描述：给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1：输入: prices = [3,3,5,0,0,3,1,4] → 输出: 6（第4天买入第6天卖出利润3，第7天买入第8天卖出利润3，总利润6）
# 示例 2：输入: prices = [1,2,3,4,5] → 输出: 4（第1天买入第5天卖出，总利润4）
# 示例 3：输入: prices = [7,6,4,3,1] → 输出: 0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy_price = float('inf')
        total_cost = float('inf')
        profit = 0
        total_profit = 0

        for price in prices:
            buy_price = min(buy_price, price)
            profit = max(profit, price - buy_price)
            total_cost = min(total_cost, price - profit)
            total_profit = max(total_profit, price - total_cost)

        return total_profit
