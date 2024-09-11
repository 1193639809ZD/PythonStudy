# @Author: eveleaf
# @Date: 2024-09-05 15:27
# @LastEditTime: 2024-09-08 15:12
# @Description:

n = int(input())

nums = [int(item) for item in input().split(" ")]

cnts = [0] * n
for i in range(1, n + 1):
    for j in range(n - i + 1):
        for k in range(i):
            cnts[j + k] += 1

cnts.sort(reverse=True)
nums.sort()

ans = 0
for i in range(n):
    ans += nums[i] * cnts[i]

print(ans)
