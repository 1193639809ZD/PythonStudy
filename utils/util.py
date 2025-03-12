# @Author: eveleaf
# @Date: 2024-10-21 11:05
# @LastEditTime: 2024-10-21 11:06
# @Description:


def lclogging(tech):
    def wrapper(func):
        print(f"知识点:{tech}")

        def inner_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return inner_wrapper

    return wrapper
