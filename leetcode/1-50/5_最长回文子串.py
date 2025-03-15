class Solution:
    # 循环便利每一个字串
    # def longestPalindrome(self, s: str) -> str:
    #     def isPalindrome(s: str) -> bool:
    #         for i in range(len(s) // 2):
    #             if s[i] != s[-(i + 1)]:
    #                 return False
    #         return True
    #
    #     max_len = 1
    #     ans = ""
    #     for i in range(len(s)):
    #         for j in range(i + max_len, len(s) + 1):
    #             if isPalindrome(s[i:j]):
    #                 ans = s[i:j]
    #                 max_len = len(ans)
    #     return ans

    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len, begin = 1, 0
        # 设计状态：dp[i][j]表示s[i..j]是否是回文串，并初始化为False
        dp = [[False] * n for _ in range(n)]
        # 单个字符均为回文串
        for i in range(n):
            dp[i][i] = True

        # 从长度2开始遍历
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                # 由L和i确定右边界
                j = L + i - 1

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 包括L=2、3两种情况，只需要边界相等即可
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


if __name__ == '__main__':
    solution = Solution()
    string = "babad"
    print(solution.longestPalindrome(string))
