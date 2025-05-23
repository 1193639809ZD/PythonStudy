# @Author: eveleaf
# @Date: 2024-08-06 09:28
# @LastEditTime: 2024-08-17 10:42
# @Description: 简单说明修饰器'@'的功能，以及用法


# 修饰器，接收一个函数，返回一个新的函数
def debug(func):
    """基本装饰器示例

    Arguments:
        func -- 传入的函数

    Returns:
        返回的函数
    """

    # 创建一个新的函数
    # 修饰器如果要适配多种函数，一般是传入可变参数，*args, **kwargs
    def warpper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)

    # 返回新创建的函数
    return warpper


# 带参数的修饰器
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter {func}()".format(level=level, func=func.__name__))
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@debug
def say_hello():
    print("hello!")


@debug
def say(words):
    print(words)


@logging(level="Warning")
def say_level(words):
    print(words)


if __name__ == "__main__":
    say_hello()
    say("program end!")
    say_level("debug level")
