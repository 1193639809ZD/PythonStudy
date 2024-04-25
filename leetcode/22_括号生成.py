from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            # 回溯主体
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            # 回溯尝试
            if left < n:
                backtrack(S + ["("], left + 1, right)
            if right < left:
                backtrack(S + [")"], left, right + 1)

        backtrack([], 0, 0)
        return ans
