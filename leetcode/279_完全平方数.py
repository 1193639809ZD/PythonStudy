class Solution:
    # 转化成背包问题
    def numSquares(self, n: int) -> int:
        # 预处理出需要使用的完全平方数
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i * i)
            i += 1

        # 初始化为一个较大的值，如 +inf 或 n
        dp = [n] * (n + 1)
        # 初始化
        dp[0] = 0

        # 完全背包：优化后的状态转移
        for num in nums:
            # 第一层循环：遍历nums
            for j in range(num, n + 1):
                # 第二层循环：遍历背包【正序】
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[n]
