from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return 0
    #     # 当前下标
    #     cur = 0
    #     # 步数
    #     step = 0
    #     while cur + nums[cur] < len(nums) - 1:
    #         # 可以走的距离
    #         distance = 0
    #         for i in range(cur, cur + nums[cur] + 1):
    #             if i + nums[i] > distance:
    #                 # 更新索引和期望距离
    #                 cur = i
    #                 distance = i + nums[i]
    #         step += 1
    #     if cur == len(nums) - 1:
    #         return step
    #     else:
    #         return step + 1

    # 简洁实现
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
