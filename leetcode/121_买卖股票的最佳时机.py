from typing import List


class Solution:
    # 贪心
    def maxProfit(self, prices: List[int]) -> int:
        # 低买高卖，dp[i]记录当前最大的受益
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

    # 动态规划
    # def maxProfit(self, prices: List[int]) -> int:
    #     n = len(prices)
    #     # 低买高卖，dp[i]记录当前最大的受益
    #     dp = [0] * n
    #     min_price = prices[0]
    #     for i in range(1, n):
    #         min_price = min(min_price, prices[i])
    #         dp[i] = max(dp[i - 1], prices[i] - min_price)
    #
    #     return dp[n - 1]
