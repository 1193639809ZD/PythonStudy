# @Author: eveleaf
# @Date: 2024-11-01 20:53
# @LastEditTime: 2024-11-08 11:31
# @Description:

# @Author: eveleaf
# @Date: 2024-11-01 20:53
# @LastEditTime: 2024-11-01 20:53
# @Description: 图的节点之间的距离

from typing import List


class Solution:
    # 图的节点到某个点的最短距离，有向图
    # 特殊条件：箭头的颜色要交替进行，比如a到b蓝色，b到c是红色，或者反过来，交替进行
    # 0到0点的距离为0

    # 广度优先搜索
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        # 图的邻接表，0和1表示不同颜色的边
        graph = [[] for _ in range(n)]
        for x, y in redEdges:
            graph[x].append((y, 0))
        for x, y in blueEdges:
            graph[x].append((y, 1))
        # 初始化为-1，即无法到达
        distances = [-1] * n
        # 用来存储已经搜索过的节点，以及当前边的颜色
        visited = {(0, 0), (0, 1)}
        # 用来存储当前搜索到的节点，以及当前边的颜色，(x, color)，x表示点，color表示颜色
        # 表示：到0点颜色为0，到0点颜色为1
        q = [(0, 0), (0, 1)]
        # 当前距离0点的距离，因为bfs第一次访问的距离就是最短距离，因此直接赋值即可，不需要比较
        distance = 0
        while q:
            tmp = q
            q = []
            # x是目标节点，color是颜色
            for x, color in tmp:
                # 距离如果没有更新过，直接更新
                if distances[x] == -1:
                    distances[x] = distance
                for p in graph[x]:
                    # 颜色与当前颜色不对，且该边没有访问过
                    if p[1] != color and p not in visited:
                        visited.add(p)
                        q.append(p)
            distance += 1
        return distances
