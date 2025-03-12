# @Author: eveleaf
# @Date: 2024-08-27 09:32
# @LastEditTime: 2024-11-08 11:33
# @Description: 关于函数参数的说明


def func1(a, b):
    print(a, b)


def func2(a, b="world"):
    print(a, b)


def func3(a, b, *args, **kwargs):
    print(a, b)

    print(f"args type: {type(args)}")
    if not args:
        print("args is null")
    else:
        print(args)

    print(f"kwargs type: {type(kwargs)}")
    if not kwargs:
        print("kwargs is null")
    else:
        print(kwargs)


if __name__ == "__main__":
    # func1("hello", "world")
    # func2("eveleaf")
    # func3("hello")
    # func3("hello", "eveleaf", "kirto")
    func3("hello", *(3, 4), **{"n1": "eveleaf", "n2": "kirto"})
    print("hello")
