# @Author: eveleaf
# @Date: 2024-09-19 19:20
# @LastEditTime: 2024-09-19 19:21
# @Description:

# @Author: eveleaf
# @Date: 2024-09-19 19:20
# @LastEditTime: 2024-09-19 19:38
# @Description:


def remaining_numbers(n, k, m, A):
    # 先将集合 A 进行排序
    A.sort()

    # 记录当前剩余的数字数量
    remaining = n

    # 使用滑动窗口的方法找到符合条件的子数组
    i = 0
    while i + m - 1 < remaining:
        # 找到符合条件的窗口，窗口的大小是 m
        if A[i + m - 1] - A[i] <= k:
            # 删除其中的最小值，即 A[i]
            del A[i]
            remaining -= 1
            print(A)
            print(f"i: {i}, remaining: {remaining}")
        else:
            i += 1

    # 返回剩余的数字数量
    return remaining


# 示例用法
n = 5
k = 2
m = 3
A = [5, 4, 4, 2, 1]
print(remaining_numbers(n, k, m, A))
