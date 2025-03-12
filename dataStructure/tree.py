# @Author: eveleaf
# @Date: 2024-10-20 21:36
# @LastEditTime: 2024-10-20 21:38
# @Description: 树的相关操作
class Tree:
    def __init__(self, isConnected=None):
        self.isConnected = None
        self.visited = None

    # 深度优先遍历：邻接矩阵版本
    def dfs(self, cur):
        visited[cur] = True
        for j in range(len(self.isConnected)):
            if isConnected[cur][j] == 1 and visited[j] == False:
                self.dfs(j)


# 邻接矩阵
isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
visited = [False] * len(isConnected)
