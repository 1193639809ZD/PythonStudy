from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 动态规划起始条件
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        ans = [0] * len(nums)
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # 动态规划核心问题：f(n)与f(n - 1)、f(n - 2)...的关系
            ans[i] = max(ans[i - 2] + nums[i], ans[i - 1])
        return ans[n - 1]
