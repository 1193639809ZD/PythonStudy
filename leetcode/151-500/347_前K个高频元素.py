from typing import List
from collections import defaultdict


class Solution:
    # 使用hash表辅助查询
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ass_dict = defaultdict(int)

        for num in nums:
            ass_dict[num] += 1

        count = sorted(ass_dict, key=lambda x: ass_dict[x], reverse=True)
        return count[:k]
