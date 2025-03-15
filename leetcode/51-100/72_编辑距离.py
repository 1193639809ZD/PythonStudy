class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 设计状态：dp[i][j]为word1[:i]和word2[:j]的编剧距离
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 状态初始化：当字符串有一方为空时，编辑距离为另一方的长度
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 状态转移方程
                # word1删除一个字符dp[i - 1][j] + 1，word2增加一个字符dp[i][j - 1] + 1，替换一个字符dp[i - 1][j - 1] + 1
                add1 = dp[i - 1][j] + 1
                add2 = dp[i][j - 1] + 1
                if word1[i - 1] == word2[j - 1]:
                    change = dp[i - 1][j - 1]
                else:
                    change = dp[i - 1][j - 1] + 1
                dp[i][j] = min(add1, add2, change)

        return dp[-1][-1]
