from typing import List


class Solution:
    # 使用除法
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 检测nums中为0的下标
        ass_list = []
        # 总乘积
        product = 1
        for i in range(len(nums)):
            if nums[i]:
                product *= nums[i]
            else:
                ass_list.append(i)

        ans = [0 for i in range(len(nums))]
        # 如果存在0的情况
        if len(ass_list) == 1:
            ans[nums.index(0)] = product
            return ans
        if len(ass_list) > 1:
            return ans
        # 不存在0
        for i in range(len(nums)):
            ans[i] = product // nums[i]
        return ans

    # 辅助列表
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     left, right, ans = [0] * n, [0] * n, [0] * n
    #
    #     left[0] = 1
    #     for i in range(1, n):
    #         left[i] = left[i - 1] * nums[i - 1]
    #     right[n - 1] = 1
    #     for i in range(n - 2, -1, -1):
    #         right[i] = right[i + 1] * nums[i + 1]
    #
    #     for i in range(n):
    #         ans[i] = left[i] * right[i]
    #     return ans

