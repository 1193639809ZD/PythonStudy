from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, cur):
            # 回溯主体
            if sum(comb) == target:
                res.append(comb)
                return
            # 回溯尝试
            for i in range(cur, len(candidates)):
                # 剪枝1：去除重复元素，也可以给结果去重，但是容易被极端例子搞
                if i and candidates[i] == candidates[i - 1] and used[i - 1] == False:
                    continue
                # 剪枝2：comb加上当前元素如果大于target，后续组合不需要测试
                if sum(comb + [candidates[i]]) > target:
                    return
                used[i] = True
                backtrack(comb + [candidates[i]], i + 1)
                # 重置状态
                used[i] = False


        candidates.sort()
        # used的作用是防止重复
        res, used = [], [False] * len(candidates)
        backtrack([], 0)

        return res
