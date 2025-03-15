class Solution:
    # 回溯写出所有组合，然后返回对应位置的元素
    # def getPermutation(self, n: int, k: int) -> str:
    #     def backtrack(comb):
    #         # 回溯主体
    #         if len(comb) == len(nums):
    #             res.append(comb)
    #             return
    #
    #             # 回溯尝试
    #         for i in range(len(nums)):
    #             if visit[i] == False:
    #                 visit[i] = True
    #                 backtrack(comb + str(nums[i]))
    #                 visit[i] = False
    #
    #     res = []
    #     nums = [i for i in range(1, n + 1)]
    #     visit = [False for _ in range(n)]
    #     backtrack('')
    #
    #     return res[k - 1]

    # 数学推导：计算每个位置元素
    def getPermutation(self, n: int, k: int) -> str:
        # 注意0阶为1
        cnts = [1] * (n + 1)
        for i in range(1, n):
            cnts[i] = cnts[i - 1] * i

        res = ''
        nums = [i for i in range(1, n + 1)]

        for i in range(n):
            cnt = cnts[len(nums) - 1]
            index = (k - 1) // cnt

            num = nums[index]
            res = res + str(num)

            nums.remove(num)
            k = k - index * cnt

        return res
