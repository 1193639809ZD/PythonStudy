# @Author: eveleaf
# @Date: 2024-09-14 19:08
# @LastEditTime: 2024-09-14 19:10
# @Description:

import math

points = "R***B**G"

r = points.index("R")
dist = math.inf
for i in range(r - 1, -1, -1):
    if points[i] == "G" or points[i] == "B":
        dist = r - i
        break
    elif points[i] == "#":
        break
for i in range(r, len(points)):
    if points[i] == "G" or points[i] == "B":
        dist = i - r
        break
    elif points[i] == "#":
        break
if dist != math.inf:
    print(dist)
else:
    print(-1)


b = points.index("B")
dist = math.inf
for i in range(b - 1, -1, -1):
    if points[i] == "G" or points[i] == "B":
        dist = b - i
        break
    elif points[i] == "#":
        break
if dist != math.inf:
    print(dist)
else:
    print(-1)

g = points.index("G")
dist = math.inf
for i in range(r - 1, -1, -1):
    if points[i] == "G" or points[i] == "B":
        dist = min(dist, r - i)
    elif points[i] == "#":
        break
if dist != math.inf:
    print(dist)
else:
    print(-1)
