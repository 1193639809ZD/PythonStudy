# @Author: eveleaf
# @Date: 2024-09-19 20:03
# @LastEditTime: 2024-09-19 20:03
# @Description:

import bisect


def find_max_distance(a, b, p):
    # 将人的位置数组a和通行证位置数组b排序
    a.sort()
    b.sort()

    max_distance = 0

    # 遍历每个人，计算其最短路径
    for person in a:
        # 找到离person最近的通行证
        idx = bisect.bisect_left(b, person)

        # 初始化最小的路径为无穷大
        min_distance = float("inf")

        # 检查person的左侧最近通行证
        if idx > 0:
            left_pass = b[idx - 1]
            distance = abs(person - left_pass) + abs(left_pass - p)
            min_distance = min(min_distance, distance)

        # 检查person的右侧最近通行证
        if idx < len(b):
            right_pass = b[idx]
            distance = abs(person - right_pass) + abs(right_pass - p)
            min_distance = min(min_distance, distance)

        # 更新最大距离
        max_distance = max(max_distance, min_distance)

    return max_distance


# 示例用法
a = [20, 100]  # 人的位置
b = [60, 10, 40, 80]  # 通行证的位置
p = 50  # 办公室的位置
result = find_max_distance(a, b, p)
print(result)  # 输出所有人走过的最长距离
