class Solution:
    def totalNQueens(self, n: int) -> int:
        # 轨迹
        ass_list = [[0] * n for _ in range(n)]
        # 结果
        ans = []

        # 将皇后插入当前位置
        def backtrack(cur_i, cur_j):
            # 修改记录
            change_index = list()
            if cur_i == n - 1:
                ass_list[cur_i][cur_j] = 'Q'
                # 将 ass_list 转化成指定格式，并保存结果
                ans.append(["".join(item) for item in ass_list])
                # 消除痕迹
                ass_list[cur_i][cur_j] = 0
                return
            # 写入皇后位置
            ass_list[cur_i][cur_j] = 'Q'
            change_index.append((cur_i, cur_j))
            # 行
            for j in range(n):
                if ass_list[cur_i][j] == 0:
                    ass_list[cur_i][j] = '.'
                    change_index.append((cur_i, j))
            # 列
            for i in range(cur_i + 1, n):
                if ass_list[i][cur_j] == 0:
                    ass_list[i][cur_j] = '.'
                    change_index.append((i, cur_j))
            # 对角线，只需要搜索下面即可
            i, j = cur_i + 1, cur_j + 1
            while i < n and j < n:
                if ass_list[i][j] == 0:
                    ass_list[i][j] = '.'
                    change_index.append((i, j))
                i, j = i + 1, j + 1
            i, j = cur_i + 1, cur_j - 1
            while i < n and j >= 0:
                if ass_list[i][j] == 0:
                    ass_list[i][j] = '.'
                    change_index.append((i, j))
                i, j = i + 1, j - 1
            # 索引下一行未访问位置
            for j in range(n):
                if ass_list[cur_i + 1][j] == 0:
                    backtrack(cur_i + 1, j)
            # 去除修改
            for i, j in change_index:
                ass_list[i][j] = 0

        for j in range(n):
            backtrack(0, j)

        return len(ans)
