from typing import List


# 涉及知识点：图的入度和出度
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 法官的入度为n-1，出度为0
        inDegrees = [0] * (n + 1)
        outDegrees = [0] * (n + 1)

        for a, b in trust:
            inDegrees[b] += 1
            outDegrees[a] += 1

        # n=1时0号也符号条件，但是0号不是有效编号，因此要从1这个有效编号开始遍历
        for i in range(1, n + 1):
            if inDegrees[i] == n - 1 and outDegrees[i] == 0:
                return i

        return -1
