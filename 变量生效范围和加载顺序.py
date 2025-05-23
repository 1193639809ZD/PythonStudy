"""
author:        eveleaf <eveleaf@outlook.com.ar>
date:          2024-12-28 21:54:15
lastModified:  2024-12-28 21:54:15
"""


def my_function():
    # 局部变量
    var1 = 1
    print(global_var)


# 命名空间，如果是导入其他文件，__name__会变成文件名，因此定义在该模块中的代码只有在直接执行该文件时，才会执行
if __name__ == "__main__":
    # 定义在该模块中的变量为全局变量，但不建议这么使用，因为会导致后续理解和管理混乱，还是推荐使用参数传递
    global_var = "Hello, World!"  # 全局变量
    my_function()
