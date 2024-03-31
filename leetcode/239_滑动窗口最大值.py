from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        windows = deque()
        # 未形成窗口
        for i in range(k):
            while windows and windows[-1] < nums[i]:
                windows.pop()
            windows.append(nums[i])
        res = [windows[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if windows[0] == nums[i - k]:
                windows.popleft()
            # 删除窗口内所有小于nums[i]的元素
            while windows and windows[-1] < nums[i]:
                windows.pop()
            windows.append(nums[i])
            res.append(windows[0])
        return res
