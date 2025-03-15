class Solution(object):
    def partition(self, s):
        def targetSub(s):
            return s == s[::-1]

        def backtrack(comb, cur):
            # 回溯主体
            if cur == len(s):
                res.append(comb)
            # 回溯尝试
            for i in range(cur + 1, len(s) + 1):
                # 剪枝
                if targetSub(s[cur:i]):
                    backtrack(comb + [s[cur:i]], i)

        res, cur = [], 0
        backtrack([], cur)
        return res
