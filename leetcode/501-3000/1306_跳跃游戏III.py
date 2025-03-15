"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-08 16:27:06
lastModified:  2024-11-08 16:27:07
"""

from typing import List
from collections import deque

# 考点：图、图的遍历、BFS
# 其他：用DFS也可以，但是本题用递归并不比迭代好写，递归还更慢


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 如果当前位置的值为0，符合条件，直接返回True
        if arr[start] == 0:
            return True

        n = len(arr)
        # 访问过的点
        visited = {start}
        queue = deque([start])

        while len(queue) > 0:
            u = queue.popleft()
            # 每个下标是一个节点，可跳跃的下标就是相邻的点
            for v in [u + arr[u], u - arr[u]]:
                # 保证下标在数组范围内，并且没有被访问过
                if 0 <= v < n and v not in visited:
                    if arr[v] == 0:
                        return True
                    queue.append(v)
                    visited.add(v)

        return False
