# @Author: eveleaf
# @Date: 2024-09-12 13:40
# @LastEditTime: 2024-09-12 16:31
# @Description:

# @Author: eveleaf
# @Date: 2024-09-12 13:40
# @LastEditTime: 2024-09-12 16:39
# @Description: 图、联通节点、并查集

# 题目：
# 现在初始有一些朋友关系，存在一些事件会导致两个人淡忘了他们的朋友关系。小美想知道某一时刻中，某两人是否可以通过朋友介绍互相认识？
# 事件共有 2 种：
# 1 u v：代表编号 u 的人和编号 v 的人淡忘了他们的朋友关系。
# 2 u v：代表小美查询编号 u 的人和编号 v 的人是否能通过朋友介绍互相认识。
# 注：介绍可以有多层，比如 2 号把 1 号介绍给 3 号，然后 3 号再把 1 号介绍给 4 号，这样 1 号和 4 号就认识了。

# 输入：
# 第一行输入三个正整数n,m,q，代表总人数，初始的朋友关系数量，发生的事件数量。
# 接下来的m行，每行输入两个正整数u,v，代表初始编号u的人和编号v的人是朋友关系。
# 接下来的q行，每行输入三个正整数op,u,v，含义如题目描述所述。保证至少存在一次查询操作。

# 输出
# 对于每次 2 号操作，输出一行字符串代表查询的答案。如果编号 u 的人和编号 v 的人能通过朋友介绍互相认识，则输出"Yes"。否则输出"No"。


# n, m, q = 5, 3, 5
# initial_relationship = [[1, 2], [2, 3], [4, 5]]
# events = [[1, 1, 5], [2, 1, 3], [2, 1, 4], [1, 1, 2], [2, 1, 3]]


from dataStructure import UnionFind


n, m, q = map(int, input().split(" "))

initial_relationship = []
for _ in range(m):
    initial_relationship.append([int(item) for item in input().split(" ")])

events = []
for _ in range(n):
    events.append([int(item) for item in input().split(" ")])


unionFind = UnionFind(n + 1)
relationship = set()
for relation in initial_relationship:
    relationship.add(tuple(sorted(relation)))  # 排序元素，保证关系不重复
for event in events:
    if event[0] == 1:
        relationship.discard(tuple(sorted(event[1:])))

# 将所有未被淡忘的关系加入并查集
for relation in relationship:
    unionFind.merge(*relation)

# 倒推事件，出现淡忘关系，将该关系加入并查集
ans = []
for event in events[::-1]:
    if event[0] == 1:
        unionFind.merge(event[1], event[2])
    else:
        ans.append("Yes" if unionFind.find(event[1]) == unionFind.find(event[2]) else "No")


# 逆序输出结果
for item in ans[::-1]:
    print(item)
