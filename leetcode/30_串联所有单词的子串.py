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
