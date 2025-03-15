from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(comb, cur):
            # 回溯主体
            if len(comb) == len(digits):
                res.append(comb)
                return
            # 回溯尝试
            for c in phoneMap[digits[cur]]:
                backtrack(comb + c, cur + 1)

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # 如果digits为空，直接返回
        if not digits:
            return []
        res = []
        backtrack("", 0)
        return res
