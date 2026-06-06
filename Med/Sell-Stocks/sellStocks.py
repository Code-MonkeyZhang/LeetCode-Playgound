# LeetCode 122 — 买卖股票的最佳时机 II
#
# 题目描述：给你一个整数数组 prices，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。
# 你也可以先购买然后在同一天出售。返回你能获得的最大利润。
#
# 示例 1：输入: prices = [7,1,5,3,6,4] → 输出: 7（第2天买入第3天卖出利润4，第4天买入第5天卖出利润3，总利润7）
# 示例 2：输入: prices = [1,2,3,4,5] → 输出: 4（第1天买入第5天卖出，总利润4）
# 示例 3：输入: prices = [7,6,4,3,1] → 输出: 0

def maxProfit(prices):

    return 0


if __name__ == '__main__':
    """
    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Total profit is 4 + 3 = 7.
    
    Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Total profit is 4.
    
    Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
    """
    # print(intToRoman(3))
    # print(intToRoman(58))
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print("Hello")
