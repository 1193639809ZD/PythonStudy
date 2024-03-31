from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs()
                    used[i] = False
                    path.pop()

        n = len(nums)
        # 注意used的使用，是为了保证nums的数值读取正确
        used = [False for _ in range(n)]
        res = []
        path = []
        dfs()
        return res
