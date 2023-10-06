import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import torch

# 准备数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
y2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
y3 = torch.arange(10)
y4 = torch.randn(10)

# 打印数据
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
# 设置参数
plt.xlabel('input')
plt.ylabel('output')
plt.title('matlplotlib1')
plt.legend(['PF', 'FBNQ', 'arange', 'randn'])
# 显示
plt.show()
confusion_matrix()