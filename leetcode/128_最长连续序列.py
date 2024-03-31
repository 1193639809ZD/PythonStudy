from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)

        for num in num_set:
            # 重置，遍历过的直接跳过
            if num - 1 not in num_set:
                cur_num = num
                current_streak = 1

                while cur_num + 1 in num_set:
                    cur_num += 1
                    current_streak += 1

                ans = max(ans, current_streak)

        return ans
