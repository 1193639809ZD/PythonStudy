from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 状态设计: dp[i][j]表示位置(i, j)的最小路径和
        dp = [[0] * len(grid[0]) for i in range(len(grid))]

        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
