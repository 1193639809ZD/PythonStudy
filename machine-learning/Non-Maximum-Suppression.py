import numpy as np


def non_max_suppression(boxes, scores, threshold):
    """
    非极大值抑制算法实现

    参数:
    boxes: 边界框的坐标，形状为 (N, 4)，其中 N 是边界框的数量，每个边界框由 (x_min, y_min, x_max, y_max) 表示。
    scores: 每个边界框的得分，形状为 (N,)
    threshold: 重叠阈值，用于决定是否保留边界框

    返回:
    kept_indices: 保留的边界框的索引列表
    """
    if len(boxes) == 0:
        return []

    # 计算每个边界框的面积
    area = (boxes[:, 2] - boxes[:, 0] + 1) * (boxes[:, 3] - boxes[:, 1] + 1)

    # 对得分进行排序，同时得到排序后的索引
    order = scores.argsort()[::-1]

    kept_indices = []
    while len(order) > 0:
        # 保留得分最高的边界框
        max_index = order[0]
        kept_indices.append(max_index)

        # 计算与当前最大得分边界框的重叠区域
        xx1 = np.maximum(boxes[max_index, 0], boxes[order[1:], 0])
        yy1 = np.maximum(boxes[max_index, 1], boxes[order[1:], 1])
        xx2 = np.minimum(boxes[max_index, 2], boxes[order[1:], 2])
        yy2 = np.minimum(boxes[max_index, 3], boxes[order[1:], 3])

        # 计算重叠区域的宽度和高度，注意取最大值时可能出现负数
        width = np.maximum(0.0, xx2 - xx1 + 1)
        height = np.maximum(0.0, yy2 - yy1 + 1)

        # 计算重叠区域的面积
        intersection = width * height

        # 计算 IoU（重叠区域与两个边界框面积之比）
        iou = intersection / (area[max_index] + area[order[1:]] - intersection)

        # 找到 IoU 小于阈值的边界框索引
        suppressed_indices = np.where(iou <= threshold)[0]

        # 更新 order 数组，去掉被抑制的边界框
        order = order[suppressed_indices + 1]

    return kept_indices


# 示例用法
boxes = np.array([
    [10, 20, 50, 60],
    [15, 25, 55, 65],
    [30, 40, 70, 80]
])
scores = np.array([0.9, 0.75, 0.8])

threshold = 0.5
kept_indices = non_max_suppression(boxes, scores, threshold)
print("保留的边界框索引:", kept_indices)
print("保留的边界框:", boxes[kept_indices])

np.random.random()
