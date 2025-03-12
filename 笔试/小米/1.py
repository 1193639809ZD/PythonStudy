# @Author: eveleaf
# @Date: 2024-09-19 16:40
# @LastEditTime: 2024-09-19 16:44
# @Description:


def dfs(comb, cur):
    if sum(comb) >= N - c:
        return True
    if sum(comb) > N:
        return False

    for i in range(cur, n):
        if dfs(comb + [toys[i]], i + 1):
            return True

    return False


N, n, c = 10, 1, 3
toys = [6]
if dfs([], 0):
    print("YES")
else:
    print("NO")
