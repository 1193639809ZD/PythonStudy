# @Author: eveleaf
# @Date: 2024-09-13 08:50
# @LastEditTime: 2024-09-13 08:52
# @Description:

# 题目：定义一个数组a的权值计算如下：首先将a的每一对相邻两项求和，得到一个b数组。那么b数组的最大值减最小值即为a数组的权值。要求构造一个长度为n的排列，满足权值尽可能小。

# 思路：按照顺序大小，交替输出即可，确保最小值和最大值相邻，如[1, 7, 2, 6, 3, 5, 4]


def calculate_weight(arr):
    """计算给定数组的权值"""
    b = [arr[i] + arr[i + 1] for i in range(len(arr) - 1)]
    return max(b) - min(b)


def construct_permutation(n):
    """构造一个长度为n的排列，使其权值尽可能小"""
    permutation = [0] * n
    for i in range(n):
        if i % 2 == 0:
            permutation[i] = i // 2 + 1
        else:
            permutation[i] = n - (i // 2)

    return permutation


# 示例输入
n = int(input())

# 构造排列
permutation = construct_permutation(n)

# 计算权值
weight = calculate_weight(permutation)

for num in permutation:
    print(num, end=" ")
