from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """滑动窗口

        Args:
            nums (List[int]): 数组

        Returns:
            int: 最大连续和
        """
        # 最大连续和
        ans = nums[0]
        # 窗口和，改进版，建立滑动窗口的目的是为了获取最大连续数组的和，那么只要设立一个变量模拟这个行为即可。
        windows = 0
        for i in range(len(nums)):
            # 更新窗口和
            windows += nums[i]
            # ans 更新条件
            if windows > ans:
                ans = windows
            # 窗口和为负数，则清零
            if windows < 0:
                windows = 0
        return ans

    def greedy(self, nums: List[int]) -> int:
        """贪心算法

        Args:
            nums (List[int]): 数组

        Returns:
            int: 最大连续和
        """
        ans = nums[0]
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans
