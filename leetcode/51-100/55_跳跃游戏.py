from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, cur, distance = len(nums), 0, 0
        while cur <= distance:
            distance = max(distance, cur + nums[cur])
            if distance >= n - 1:
                return True
            cur += 1
        return False
