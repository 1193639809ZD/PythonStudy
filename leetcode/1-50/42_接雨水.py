from typing import List


class Solution:
    # 动态规划
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
    #     获取当前元素左右两侧的最大值
    #     n = len(height)
    #     leftMax = [height[0]] + [0] * (n - 1)
    #     for i in range(1, n):
    #         leftMax[i] = max(leftMax[i - 1], height[i])
    #
    #     rightMax = [0] * (n - 1) + [height[n - 1]]
    #     for i in range(n - 2, -1, -1):
    #         rightMax[i] = max(rightMax[i + 1], height[i])
    #
    #     ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
    #     return ans

    def trap(self, height: List[int]) -> int:
        """
        对于下标i，下雨后水能到达的最大高度等于下标i两边的最大高度的最小值，下标i处能接的雨水量等于下标i处的水能到达的最大高度减去height[i]

        :param height:
        :return:
        """
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        while left < right:
            # 如果leaf小于right，那么left最大的元素一定小于right，因为只有小于时才移动
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                right -= 1

        return ans
