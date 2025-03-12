# @Author: eveleaf
# @Date: 2024-09-13 15:27
# @LastEditTime: 2024-09-13 15:27
# @Description:


def count_task_distributions(n, x, y, z):
    count = 0
    for a in range(min(x, n) + 1):
        for b in range(min(y, n - a) + 1):
            c = n - a - b
            if 0 <= c <= z:
                count += 1
    return count


print(count_task_distributions(5, 2, 3, 1))
