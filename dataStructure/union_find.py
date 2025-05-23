# @Author: eveleaf
# @Date: 2024-09-12 14:46
# @LastEditTime: 2024-09-12 14:50
# @Description: 并查集


class UnionFind:
    # 初始化
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]

    # 查找
    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            # 压缩路径，并递归查找父节点
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    # 合并
    def merge(self, i, j):
        self.parent[self.find(i)] = self.find(j)
