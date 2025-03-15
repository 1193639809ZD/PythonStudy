# @Author: eveleaf
# @Date: 2024-08-27 10:50
# @LastEditTime: 2024-09-04 13:55
# @Description: 子串组合，子串位置查找

from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m, n, ls = len(words), len(words[0]), len(s)
        # 从每个起始位置遍历
        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter()
            # 初始化窗口
            for j in range(m):
                word = s[i + j * n : i + (j + 1) * n]
                differ[word] += 1
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            # 开始遍历
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n : start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        # 如果word没有次数耗尽，删除，便于后续成功条件判断
                        del differ[word]
                    word = s[start - n : start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    res.append(start)
        return res

    # 简单方法：先找组合，再找位置，计算复杂度高，超时
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     # 利用递归找到所有的子串组合
    #     def dfs(comb, cur):
    #         # 递归出口
    #         if cur == len(words):
    #             combs.add(comb)
    #             return

    #         for i in range(len(words)):
    #             if visited[i] == False:
    #                 visited[i] = True
    #                 dfs(comb + words[i], cur + 1)
    #                 visited[i] = False

    #     # 找到所有子串组合，利用set性质，可以避免重复组合
    #     combs = set()
    #     visited = [False] * len(words)
    #     dfs("", 0)
    #     # 打印一下组合结果
    #     print(combs)

    #     # 逐个查找组合的起始地址
    #     ans = set()
    #     lc = len(words) * len(words[0])
    #     for i in range(len(s) - lc + 1):
    #         if s[i : i + lc] in combs:
    #             ans.add(i)

    #     return list(ans)


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    )
