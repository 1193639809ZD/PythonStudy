from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtracking(cur, dots, curIP):
            # 回溯主体
            # 点到第4点且已经走到字符串尾时，去除最后一点并添加到res中
            if dots == 4 and cur == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            # 回溯尝试
            # 剪枝：每个点最多移动3次，且不能移动超过字符串
            for i in range(cur, min(cur + 3, len(s))):
                # 判断IP段是否合法
                if int(s[cur: i + 1]) < 256 and (s[cur] != "0" or cur == i):
                    backtracking(i + 1, dots + 1, curIP + s[cur: i + 1] + ".")

        # 无效字符
        if not s or len(s) < 4 or len(s) > 12:
            return []

        res = []
        backtracking(0, 0, "")
        return res
