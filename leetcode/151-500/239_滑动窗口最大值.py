from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        windows = deque()
        for i in range(k):
            # 使用单调栈减少比较次数
            # 因为可能有重复的最大值，所以只有小于时才弹出元素，保证当最左侧的过期后，依然有个最大值
            while windows and windows[-1] < nums[i]:
                windows.pop()
            windows.append(nums[i])
        res = [windows[0]]
        for i in range(k, len(nums)):
            if windows[0] == nums[i - k]:
                windows.popleft()
            while windows and windows[-1] < nums[i]:
                windows.pop()
            windows.append(nums[i])
            res.append(windows[0])
        return res

    # 滑动窗口、暴力
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums or k == 0:
    #         return []
    #     windows = deque()
    #     # 未形成窗口
    #     for i in range(k):
    #         windows.append(nums[i])
    #     res = [max(windows)]
    #     # 形成窗口后
    #     for i in range(k, len(nums)):
    #         windows.popleft()
    #         windows.append(nums[i])
    #         res.append(max(windows))
    #     return res
