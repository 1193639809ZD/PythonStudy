from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        """
        回溯：每次有序挑选数组内2个数进行四则运算，并把这个2个数去除，将结果添加到数组中，直到数组只有一个数，判断结果是否为24
        """
        target = 24
        epsilon = 1e-6
        add, multiply, subtract, divide = 0, 1, 2, 3

        def backtrack(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - target) < epsilon
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == add:
                                newNums.append(x + y)
                            elif k == multiply:
                                newNums.append(x * y)
                            elif k == subtract:
                                newNums.append(x - y)
                            elif k == divide:
                                if abs(y) < epsilon:
                                    continue
                                newNums.append(x / y)
                            # 如果返回结果是bool类型，这种写法可以减少判断代码
                            if backtrack(newNums):
                                return True
                            newNums.pop()
            return False

        return backtrack(nums)
