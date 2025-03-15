class Solution:
    # 转化成背包问题
    def numSquares(self, n: int) -> int:
        """
        解决思路：完全背包问题，物品平方数，重量数值，价值均为1，背包完全平方数，求解装满背包时，价值最低
        """

        # 物品：完全平方数
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i * i)
            i += 1

        # 设计状态：dp[n]为和为n的最小平方数个数，初始化为 +inf，dp[0]=0
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # 先遍历物品
        for num in nums:
            # 后遍历背包
            for j in range(num, n + 1):
                # dp[j] = function(dp[j], dp[j - weight[i]] + value[i])
                # 这里function是取最小值
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[-1]
