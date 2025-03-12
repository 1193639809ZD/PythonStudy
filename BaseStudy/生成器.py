# @Author: eveleaf
# @Date: 2024-09-10 09:44
# @LastEditTime: 2024-09-11 21:54
# @Description:

# @Author: eveleaf
# @Date: 2024-09-10 09:44
# @LastEditTime: 2024-09-14 15:56
# @Description:


# def gen():
#     yield 1
#     yield 2


# f = gen()


# print(f"1: {f.__next__()}")
# print(f"2: {f.__next__()}")
# print(f"3: {f.__next__()}")
# class Truth:
#     pass


# x = Truth()
# print(bool(x))


# class Animal:
#     num = 0

#     def __getattr__(self):
#         return 1

#     def __init__(self) -> None:
#         pass


# animal = Animal()
# print(animal.num)


# nums = [1, 2, 3, 4, 5]

# dp = [0] * len(nums)
# for i in range(len(nums)):
#     if i == 0:
#         dp[i] = nums[i]
#     else:
#         dp[i] = nums[i] + dp[i - 1]

# res = float("inf")
# for i in range(len(nums) - 1):
#     res = min(res, (dp[-1] - dp[i]) * dp[i])

# print(res)
# print(dp[-1])
