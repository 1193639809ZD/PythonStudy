from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        算法思想：贪心
        解题思路：area = (right - left) * min(height[right], height[left])
            1. 暴力：通过分析可知，面积只与左右下标有关，即求取最大面积对应的下标，通过暴力遍历左右下标组合即可求取最大面积，
            2. 剪枝：若height[left] < height[right]，对于left，与right往中心移动的所有组合，均不可能超过现在，即left作为结果下标之一的
            情况被排除，通过这种方式，每次比较均可排除一个下标。
                - 局部最优：对于left来说，当前结果就是最优的
                - 全局最优：通过不断更新left，right之间的较小值，来搜索全局的面积最大值
        """
        left, right = 0, len(height) - 1
        ans = 0

        while right > left:
            # 更新结果
            ans = max(ans, min(height[right], height[left]) * (right - left))
            # 判断左右指针如何移动
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans
