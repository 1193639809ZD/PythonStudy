from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        算法：贪心
        解题思路：
            - 局部最优：每一跳均取得期望的最大值
            - 全局最优：最少的跳数
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                # 遍历每一跳期望的最大值
                if i == end:
                    end = maxPos
                    step += 1
        return step
