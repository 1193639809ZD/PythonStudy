from typing import List


class Solution:
    # 正常算法
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     ass_list = [0 for _ in range(n + 1)]
    #     for num in nums:
    #         if num <= 0 or num > n:
    #             continue
    #         else:
    #             ass_list[num] = 1
    #
    #     for i in range(1, n + 1):
    #         if ass_list[i] == 0:
    #             return i
    #     return n + 1

    # 利用set的性质，可以快速建立查询表
    def firstMissingPositive(self, nums: List[int]) -> int:
        ass_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in ass_set:
                return i
        return len(nums) + 1
