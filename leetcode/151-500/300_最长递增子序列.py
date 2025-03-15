from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 递推式：f(n) = 小于该数的最长子序列长度 + 1
        # 起始值：默认值1
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            # max_len：记录小于该数的最长子序列长度
            max_len = 0
            for j in range(i):
                if nums[i] > nums[j] and max_len < res[j]:
                    max_len = res[j]
            res[i] = max_len + 1

        return max(res)
