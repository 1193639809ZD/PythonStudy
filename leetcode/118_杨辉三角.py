from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]

        cur = 2
        while cur < numRows:
            temp = [1]
            for i in range(len(ans[cur - 1]) - 1):
                temp.append(ans[cur - 1][i] + ans[cur - 1][i + 1])
            temp.append(1)
            ans.append(temp)
            cur += 1
        return ans
