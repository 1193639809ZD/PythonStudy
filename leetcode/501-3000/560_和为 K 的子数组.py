from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        # 哈希表，前缀和：出现次数
        pre_fix, hash_map = 0, defaultdict(int)
        hash_map[0] = 1

        for num in nums:
            pre_fix += num
            ans += hash_map[pre_fix - k]
            hash_map[pre_fix] += 1

        return ans
