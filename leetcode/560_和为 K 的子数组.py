from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        prefix_sum = 0
        count = 0
        # 哈希表，前缀和：出现次数
        hash_map = defaultdict(int)
        hash_map[0] = 1
        n = len(nums)
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum - k in hash_map:
                count += hash_map[prefix_sum - k]
            hash_map[prefix_sum] += 1
        return count
