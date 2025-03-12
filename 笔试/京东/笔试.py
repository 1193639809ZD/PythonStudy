# import functools

# dict = {}
# s = "abcdefghigklmnopqrstuvwxyz"
# for i in range(len(s)):
#     dict[s[i]] = i
# # print(dict)


# def sort_str(s1: str, s2: str):
#     if s2.startswith(s1):
#         return -1
#     elif s1.startswith(s2):
#         return 1

#     for i in range(min(len(s1), len(s2))):
#         if s1[i] != s2[i]:
#             return dict[s1[i]] - dict[s2[i]]
#     # return 0


# strs = ["aaa", "aaaa", "aac"]

# strs.sort(key=functools.cmp_to_key(sort_str))
# print(strs)

import math


# 辅助函数：计算两点之间的欧几里得距离
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Kruskal算法中的Union-Find辅助类
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Kruskal算法构建最小生成树并返回其中最长的边
def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])  # 按照边权重排序
    mst_max_edge = 0  # 记录最小生成树中的最长边
    mst_edges = 0  # 记录最小生成树中的边数

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_max_edge = max(mst_max_edge, weight)
            mst_edges += 1
            if mst_edges == n - 1:  # 最小生成树有n-1条边
                break

    return mst_max_edge


# 主函数：计算最小生成树中最长的边
def longest_shortest_distance(points):
    n = len(points)
    edges = []

    # 计算所有点对之间的距离，构成边集
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            edges.append((i, j, dist))

    # 使用Kruskal算法构造最小生成树并找到最长的边
    return kruskal(n, edges)


# 测试
points = [(0, 0), (0, 5), (6, 0)]
result = longest_shortest_distance(points)
print(result)
