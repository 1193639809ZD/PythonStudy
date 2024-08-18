# @Author: eveleaf
# @Date: 2024-08-18 15:00
# @LastEditTime: 2024-08-18 15:04
# @Description: 正则表达式，动态规划


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                # 特例：*可以匹配0个*，==> "**" match ""
                if p[j - 1] == "*":
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == "__main__":
    sol = Solution()

    s = ""
    p = "***"

    print(sol.isMatch(s, p))
