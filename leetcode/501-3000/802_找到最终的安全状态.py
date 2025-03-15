# @Author: eveleaf
# @Date: 2024-10-24 13:57
# @LastEditTime: 2024-10-24 13:58
# @Description: 拓扑排序、深度优先搜索 + 三色标记法

from typing import List
from collections import deque
from utils.util import lclogging


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        深度优先搜索 + 三色标记法 单向箭头
        graph：[[1,2],[2,3],[5],[0],[5],[],[]]

        输出：[2,4,5,6]
        时间复杂度：O(n+m)，
        空间复杂度：O(n)
        """

        def safe(x: int) -> bool:
            # 三色：0 未访问，1 该节点位于递归栈中，或者在某个环上；，2 该节点搜索完毕，是一个安全节点。
            # 再次访问，有2种情况：1. 该节点在递归栈中，说明该节点在某个环上，返回False；2. 该节点搜索完毕，是一个安全节点，返回True。
            if color[x] > 0:
                return color[x] == 2
            # 第一次访问，放入栈种，赋值为1
            color[x] = 1
            # 遍历所有出边
            for y in graph[x]:
                if not safe(y):
                    return False
            # 搜索完毕，如果不存在环路，赋值为2，设为安全节点
            color[x] = 2
            return True

        n = len(graph)
        # 初始化为0
        color = [0] * n
        return [i for i in range(n) if safe(i)]

    @lclogging("拓扑排序")
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 时间复杂度：O(n+m)
        # 空间复杂度：O(n+m)
        # 逆邻接表
        rg = [[] for _ in graph]
        for x, ys in enumerate(graph):
            for y in ys:
                rg[y].append(x)
        # 逆邻接表的入度列表
        in_deg = [len(ys) for ys in graph]
        # 队列放入入度为0的点
        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        # 遍历队列
        while q:
            for x in rg[q.popleft()]:
                in_deg[x] -= 1
                # 入度为0，放入队列
                if in_deg[x] == 0:
                    q.append(x)

        return [i for i, d in enumerate(in_deg) if d == 0]
