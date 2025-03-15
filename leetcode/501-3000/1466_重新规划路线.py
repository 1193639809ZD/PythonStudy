# @Author: eveleaf
# @Date: 2024-11-08 10:30
# @LastEditTime: 2024-11-08 10:30
# @Description: 图的遍历，在遍历的过程中，加一些操作，简单来说是记录正向的边的数量

# 解决方法：将有向边改为无向边，判断边的类型，注意跳过父节点
from typing import List


class Solution:
    def dfs(self, x: int, parent: int, e: List[List[List[int]]]) -> int:
        # 遍历邻接表，遇到1的res加1
        res = 0
        for edge in e[x]:
            # 父节点跳过
            if edge[0] == parent:
                continue
            # edge[0]是子节点，edge[1]为0或1，1是目标，0对res无影响，因此可以直接加edge[1]
            # x是递归的父节点
            res += edge[1] + self.dfs(edge[0], x, e)
        return res

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # graph是邻接表
        graph = [[] for _ in range(n)]
        for edge in connections:
            # 添加所有的子节点，其中1表示可以到达，0表示无法到达，即反方向，一条边两端节点都要添加
            graph[edge[0]].append([edge[1], 1])
            graph[edge[1]].append([edge[0], 0])
        return self.dfs(0, -1, graph)
