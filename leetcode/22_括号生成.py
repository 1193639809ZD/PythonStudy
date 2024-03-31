from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        # left、right监控左右括号数量
        def backtrack(S, left, right):
            # 回溯指标
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            # 剪枝条件
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            # 剪枝条件
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans
