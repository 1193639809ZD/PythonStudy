"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-11-08 16:09:21
lastModified:  2024-11-08 16:09:22
"""

from typing import List
from collections import deque

"""
433. 最小基因变化
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

考点：BFS、最短路径、树
注意点：
    1. 节点的子节点，是该节点变动1个字符的所有节点，如果是8个字符，每个字符3中变化，就是24个子节点，其中只有在bank中的才是合法的子节点
    2. 节点是唯一的，也就是说搜索过的节点，不要再次搜索

"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 如果没有变化，返回0
        if start == end:
            return 0
        # 将band变为hash表，加速查询
        bank = set(bank)
        # 如果end不在bank中，不合法，直接返回-1
        if end not in bank:
            return -1
        # 进行BFS
        queue = deque([(start, 0)])
        while queue:
            # cur是当前节点，step是当前节点的步数
            cur, step = queue.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        comb = cur[:i] + y + cur[i + 1 :]
                        if comb in bank:
                            # 因为是最短路径，找到直接进行返回
                            if comb == end:
                                return step + 1
                            bank.remove(comb)
                            queue.append((comb, step + 1))
        return -1
