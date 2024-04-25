class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 状态设计：dp[i][j]表示下标（i，j）的路径数目
        dp = [[0] * n for _ in range(m)]
        # 初始状态：第1行、第1列 均为1
        for i in range(m): dp[i][0] = 1
        for j in range(n): dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                # 状态转移方程
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
