from collections import Counter

a = "114514"
b = "1919810"
c = "454"
d = "9980"

da = Counter(a)
db = Counter(b)
dc = Counter(c)
dd = Counter(d)

print(da - dc)
print(db - dd)

print((da - dc) == (db - dd))
