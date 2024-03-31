from typing import List
import random


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort(reverse=True)
    #     return nums[k - 1]

    # 快排
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            cur = random.choice(nums)
            small, equal, big = [], [], []

            for num in nums:
                if cur < num:
                    big.append(num)
                elif cur > num:
                    small.append(num)
                else:
                    equal.append(num)

            if len(big) >= k:
                return quick_select(big, k)
            elif len(nums) - len(small) < k:
                return quick_select(small, k - len(nums) + len(small))
            else:
                return cur

        return quick_select(nums, k)
