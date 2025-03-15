"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-09 14:39:35
lastModified:  2024-11-09 14:39:36
"""

from typing import List
from collections import deque

# 考点：二分图染色


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                queue = deque([i])
                color[i] = RED
                while queue:
                    node = queue.popleft()
                    # 颜色翻转
                    cur_color = GREEN if color[node] == RED else RED
                    for neighbor in graph[node]:
                        # 没有染色，入队列
                        if color[neighbor] == UNCOLORED:
                            queue.append(neighbor)
                            color[neighbor] = cur_color
                        # 如果有颜色，必须是翻转颜色
                        elif color[neighbor] != cur_color:
                            return False

        return True
