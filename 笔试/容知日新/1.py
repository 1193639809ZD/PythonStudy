# @Author: eveleaf
# @Date: 2024-09-19 21:21
# @LastEditTime: 2024-09-19 21:21
# @Description:

from collections import deque


def maxSlidingWindow(nums, size):
    if not nums or size == 0:
        return []

    result = []
    dq = deque()  # 存储的是元素的索引

    for i in range(len(nums)):
        # 移除滑动窗口之外的元素
        if dq and dq[0] < i - size + 1:
            dq.popleft()

        # 移除队列中所有比当前元素小的元素，它们不可能是最大值
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # 将当前元素的索引加入队列
        dq.append(i)

        # 当窗口形成时（即i >= size - 1），将最大值加入结果
        if i >= size - 1:
            result.append(nums[dq[0]])

    return result


# 测试
nums = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
print(maxSlidingWindow(nums, size))
