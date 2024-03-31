from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return

            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                # 关键点：如果一个元素与上一个元素相同，且上一个元素在当前循环中没有使用过，说明重复了
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue
                used[i] = 1
                backtrack(path + [nums[i]])
                used[i] = 0

        nums.sort()
        res = []
        used = [0 for i in range(len(nums))]

        backtrack([])
        return res
