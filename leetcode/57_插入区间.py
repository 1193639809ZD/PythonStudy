from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 记录重合的数组下标，和插入的start和end
        remove_list = []
        pre_start, pre_end = newInterval
        for i in range(len(intervals)):
            if intervals[i][0] > pre_end or intervals[i][1] < pre_start:
                if pre_end < intervals[i][0] and pre_start > intervals[i - 1][1] and len(remove_list) == 0:
                    intervals.insert(i, [pre_start, pre_end])
                    return intervals
                elif len(remove_list):
                    break
                else:
                    continue
            else:
                pre_start = min(intervals[i][0], pre_start)
                pre_end = max(intervals[i][1], pre_end)
                remove_list.append(i)
        print(remove_list)
        # 更新数组
        if len(remove_list):
            start_index = min(remove_list)
            for _ in range(len(remove_list)):
                intervals.pop(start_index)
        elif len(intervals) == 0 or intervals[0][0] > newInterval[1]:
            start_index = 0
        else:
            start_index = len(intervals)

        intervals.insert(start_index, [pre_start, pre_end])
        return intervals
