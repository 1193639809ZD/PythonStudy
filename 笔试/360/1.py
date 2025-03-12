def max_demand_satisfaction(n, demands):
    """
    计算最多能满足多少人的需求。

    :param n: 物品的数量
    :param demands: 二维列表，每项表示一个人对两个物品的需求
    :return: 最多能满足的人数
    """
    # 初始化一个集合来记录已经分配的物品
    allocated_items = set()

    # 初始化满足人数
    satisfied_count = 0

    # 遍历每个人的需求
    for demand in demands:
        item1, item2 = demand

        # 检查这两个物品是否都没有被分配
        if item1 not in allocated_items and item2 not in allocated_items:
            # 标记这两个物品为已分配
            allocated_items.add(item1)
            allocated_items.add(item2)
            # 计数加一
            satisfied_count += 1

    return satisfied_count


# 示例数据
n = 4  # 假设有5个物品
demands = [[1, 2], [2, 3], [3, 4]]  # 每个人的需求

# 调用函数计算结果
result = max_demand_satisfaction(n, demands)
print(result)  # 输出结果
