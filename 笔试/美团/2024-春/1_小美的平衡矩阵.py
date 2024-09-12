# @Author: eveleaf
# @Date: 2024-09-11 22:40
# @LastEditTime: 2024-09-12 09:23
# @Description: 前缀和、三目运算符


# 题目：小美拿到了一个n∗n的矩阵，其中每个元素是0或者1。小美认为一个矩形区域是完美的，当且仅当该区域内0的数量恰好等于1的数量。现在，小美希望你回答有多少个i∗i的完美矩形区域。你需要回答1≤i≤n的所有答案。

# 输入：n，第一行输入一个正整数n，代表矩阵大小。接下来的n行，每行输入一个长度为n的01串，用来表示矩阵。1<=n<=200
# 举例：4 ==> 1010 ==> 0101 ==> 1100 ==> 0011

# 输出：输出n行，第i行输出i*i的完美矩形区域的数量。
# 举例：0 ==> 7 ==> 0 ==> 1


n = int(input())

nums = []
for _ in range(n):
    nums.append([int(item) for item in input()])

# 初始化前缀和矩阵
prefix0 = [[0] * (n + 1) for _ in range(n + 1)]
prefix1 = [[0] * (n + 1) for _ in range(n + 1)]


# 计算前缀和
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix0[i][j] = (
            (1 if nums[i - 1][j - 1] == 0 else 0)
            + prefix0[i - 1][j]
            + prefix0[i][j - 1]
            - prefix0[i - 1][j - 1]
        )
        prefix1[i][j] = (
            (1 if nums[i - 1][j - 1] == 1 else 0)
            + prefix1[i - 1][j]
            + prefix1[i][j - 1]
            - prefix1[i - 1][j - 1]
        )

results = [0] * (n + 1)

# 检查每个尺寸的矩形
for size in range(1, n + 1):
    count_perfect = 0
    for r1 in range(1, n - size + 2):
        for c1 in range(1, n - size + 2):
            r2 = r1 + size - 1
            c2 = c1 + size - 1

            count0 = prefix0[r2][c2] - prefix0[r1 - 1][c2] - prefix0[r2][c1 - 1] + prefix0[r1 - 1][c1 - 1]
            count1 = prefix1[r2][c2] - prefix1[r1 - 1][c2] - prefix1[r2][c1 - 1] + prefix1[r1 - 1][c1 - 1]

            if count0 == count1:
                count_perfect += 1

    results[size] = count_perfect

for i in range(len(results)):
    if i:
        print(results[i])
