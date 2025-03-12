"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-09 16:48:01
lastModified:  2024-11-09 16:48:02
"""

from collections import deque

# 图相关的函数
adj_list = [[1, 2], [2, 3], [5], [0], [5], [], []]
visited = [False] * len(adj_list)


def dfs(vertex):
    # 对访问点进行操作
    visited[vertex] = True
    # 访问相邻点
    for adj_vertex in adj_list[vertex]:
        if not visited[adj_vertex]:
            bfs(adj_vertex)


# 从vertex开始进行广度优先搜索
def bfs(vertex):
    # 创建队列，并将vertex入队
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True
    while queue:
        # 队首元素出队
        vertex = queue.popleft()
        # 对访问点进行操作
        for adj_vertex in adj_list[vertex]:
            if not visited[adj_vertex]:
                queue.append(adj_vertex)
                visited[adj_vertex] = True


# 拓扑遍历
def topology_visit(adj_list):
    # 获取入度表
    in_degs = [0] * len(adj_list)
    for vertexs in adj_list:
        for v in vertexs:
            in_degs[v] += 1
    # 将入度为0的顶点入队
    queue = deque()
    for v in range(len(in_degs)):
        if in_degs[v] == 0:
            queue.append(v)
    # 拓扑遍历
    while queue:
        vertex = queue.pop()
        # 相连的顶点的入度减一
        for v in adj_list[vertex]:
            in_degs[v] -= 1
            # 入度为0的顶点入队
            if in_degs[v] == 0:
                queue.append(v)
