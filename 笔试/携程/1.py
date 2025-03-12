def max_path_sum(n, m, k):
    # 矩阵起点值
    start_value = 0
    max_sum = 0

    # 计算路径和
    cur_i, cur_j = 0, 0  # 当前所在的坐标
    total_sum = 0
    total_sum += cur_j + cur_i * m  # 初始位置(0, 0)的值

    # 贪心地先向右或向下走
    steps = 0
    while steps < k:
        if cur_i < n - 1 and cur_j < m - 1:
            # 可以选择向下或者向右走
            if (cur_i + 1) * m + cur_j > cur_i * m + (cur_j + 1):
                # 下方的值大
                cur_i += 1
            else:
                # 右边的值大
                cur_j += 1
        elif cur_i < n - 1:
            # 只能向下走
            cur_i += 1
        elif cur_j < m - 1:
            # 只能向右走
            cur_j += 1
        else:
            # 已经到了右下角，开始来回移动
            if cur_j > 0:
                cur_j -= 1
            else:
                cur_j += 1

        # 增加当前格子的值到路径和
        total_sum += cur_j + cur_i * m
        steps += 1

    return total_sum


# 示例用法
n, m, k = 2, 2, 5  # 一个3×3的矩阵，走5步
result = max_path_sum(n, m, k)
print(result)  # 输出最大路径和
