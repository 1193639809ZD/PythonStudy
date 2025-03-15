# @Author: eveleaf eveleaf@outlook.com.ar
# @Date: 2024-11-08 11:19
# @LastEditors: eveleaf eveleaf@outlook.com.ar
# @LastEditTime: 2024-11-08 14:28
# @FilePath: /leetcode/图论/797_所有可能的路径.py
# @Description:


from typing import List


class Solution:
    # graph[i]为节点i的邻接节点组成的列表 graph = [[1,2],[3],[3],[]]
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """搜索到目标节点的所有路径

        Args:
            graph (List[List[int]]): 邻接表

        Returns:
            List[List[int]]: 到目标节点的所有路径
        """
        ans = list()
        paths = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(paths[:])
                return

            for y in graph[x]:
                paths.append(y)
                dfs(y)
                paths.pop()

        paths.append(0)
        dfs(0)
        return ans
