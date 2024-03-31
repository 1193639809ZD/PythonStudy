from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 最大连续和
    #     ans = nums[0]
    #     # 连续数组窗口
    #     window = []
    #     for i in range(len(nums)):
    #         # 向窗口添加元素
    #         window.append(nums[i])
    #         # ans 更新条件
    #         if sum(window) > ans:
    #             ans = sum(window)
    #         # 更新窗口
    #         if sum(window) < 0:
    #             window.clear()
    #     return ans

    # 改进版：建立滑动窗口的目的是为了获取最大连续数组的和，那么只要设立一个变量模拟这个行为即可。
    def maxSubArray(self, nums: List[int]) -> int:
        # 最大连续和
        ans = nums[0]
        # 窗口和
        window_sum = 0
        for i in range(len(nums)):
            # 更新窗口和
            window_sum += nums[i]
            # ans 更新条件
            if window_sum > ans:
                ans = window_sum
            # 窗口和为负数，则清零
            if window_sum < 0:
                window_sum = 0
        return ans
