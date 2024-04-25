from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        完全背包问题：
        """
        # 设计状态：dp[n]表示总金额n的组合数
        dp = [0] * (amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                # 状态转移方程：计算组合数，遍历顺序取反，可以计算排列数
                dp[j] += dp[j - coins[i]]
        return dp[amount]
