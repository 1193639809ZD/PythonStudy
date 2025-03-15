from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb):
            # 回溯主体
            if sum(comb) == target:
                res.append(comb)
                return
            if sum(comb) > target:
                return
            # 回溯尝试
            for item in candidates:
                # 剪枝1：如果comb已经添加了较大的item，那么较小的已经添加过了
                if comb and comb[-1] > item:
                    continue
                # 剪枝2：如果当前comb加上item已经大于target，后续就不需要尝试了
                if sum(comb + [item]) > target:
                    return
                backtrack(comb + [item])

        candidates.sort()
        res = []
        backtrack([])
        return res

