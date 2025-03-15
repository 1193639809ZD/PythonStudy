class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 设计状态 & 初始化
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # s & p 均为空时，可以匹配
        dp[0][0] = True
        # s为空时，只有p仅由'*'组成时，可以匹配
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 状态转移方程
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

    def isMatch(self, s: str, p: str) -> bool:
        """
        算法：贪心
        解题思路：
            1. ?和字符均是一对一映射，只有*可以匹配任何字符，那么我们只有查找字符串p中*之间的子串，是否在s中按顺序出现过
                - 局部最优：查找p的对应子串，在s中最早出现的位置，为后续匹配提供更多的可能性
                - 全局最优：p的对应子串均在s中按顺序出现，且字符串p和字符串s的结尾可以匹配

        """
        pass
