from typing import List


class Solution:
    # 回溯
    # def canPartition(self, nums: List[int]) -> bool:
    #     def backtrack(comb, cur):
    #         # 回溯主体
    #         if sum(comb) == self.target:
    #             self.flag = True
    #             return
    #         # 回溯尝试
    #         for i in range(cur, len(nums)):
    #             backtrack(comb + [nums[i]], i + 1)
    #             if self.flag:
    #                 return
    #
    #     # 是否找到组合方式
    #     self.flag = False
    #     if sum(nums) % 2 == 1:
    #         return False
    #     self.target = sum(nums) // 2
    #
    #     nums.sort()
    #     backtrack([], 0)
    #
    #     return self.flag

    # 二维数组动态规划
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:  # 总和无法等分
            return False

        target = total // 2
        if max(nums) > target:  # 最大值大于总和的一半，无法分割
            return False

        n = len(nums)

        # 初始化
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # dp[i][j]: 从前i个元素中选出若干个数字刚好能够组成j
        dp[0][0] = True  # 其他 dp[0][j]均为False

        # 状态更新
        for i in range(1, n + 1):
            for j in range(target + 1):
                # 容量有限，无法选择第i个数字nums[i-1]
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 不选nums[i-1]是dp[i - 1][j]，选择nums[i-1]是dp[i - 1][j - nums[i - 1]]，二者有一个为True即可
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]

        return dp[n][target]
