# @Author: eveleaf
# @Date: 2024-11-07 21:23
# @LastEditTime: 2024-11-07 21:23
# @Description:

from typing import List
from collections import collections


class Solution:
    # 求解树的最长路径
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 使用 defaultdict 来构建图
        g = collections.defaultdict(list)
        for i in range(n):
            g[manager[i]].append(i)

        def dfs(cur):
            res = 0
            # 遍历当前节点的邻居节点
            for ne in g[cur]:
                res = max(res, dfs(ne))
            # 返回当前节点被通知需要的时间以及所有邻居节点被通知所需的最大时间
            return informTime[cur] + res

        # 从根节点开始进行 DFS 并返回总时间
        return dfs(headID)
