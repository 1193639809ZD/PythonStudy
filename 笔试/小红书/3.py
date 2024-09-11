# @Author: eveleaf
# @Date: 2024-09-08 15:24
# @LastEditTime: 2024-09-08 15:25
# @Description:

# f(x)表示x在二进制表示下1的个数

# g(x)表示第一个比x大，且f(g(x)) = f(x)的数


# 求解最长子序列，保证bj = g(bj-1)
def g(x):
    cnt = f"{x:b}".count("1")
    for i in range(x + 1, x * 2 + 1):
        if f"{i:b}".count("1") == cnt:
            return i


n = int(input())
nums = [int(item) for item in input().split(" ")]
nums.sort()
print(nums)

dp = [1] * n
gmap = [-1] * n
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if f"{nums[j]:b}".count("1") == f"{nums[i]:b}".count("1"):
            gmap[i] = j
            break
print(gmap)

for i in range(1, n):
    if dp[gmap[i]] + 1 > dp[i]:
        dp[i] = dp[gmap[i]] + 1

print(max(dp))
