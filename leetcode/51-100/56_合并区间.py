from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        pre_start, pre_end = intervals[0]

        for pair in intervals:
            # 更新区间的情况
            if pre_end >= pair[0]:
                pre_start = min(pre_start, pair[0])
                pre_end = max(pre_end, pair[1])
            else:
                ans.append([pre_start, pre_end])
                pre_start, pre_end = pair
        ans.append([pre_start, pre_end])
        return ans
