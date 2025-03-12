# @Author: eveleaf
# @Date: 2024-09-13 15:58
# @LastEditTime: 2024-09-13 16:02
# @Description:


def smallestSufficientTeam(reqSkills, peoSkills):
    def dfs(comb, p, cur):
        if reqSkills.issubset(comb):
            ans.append(p)
            return
        for i in range(cur, len(peoSkills)):
            dfs(comb | set(peoSkills[i]), p + [i], i + 1)

    reqSkills = set(reqSkills)
    ans = []
    dfs(set(), [], 0)

    return ans


reqSkills = [5, 6, 7, 8]
peoSkills = [[2, 3, 4, 5, 6, 7, 8, 9], [5, 6, 7, 8]]

print(smallestSufficientTeam(reqSkills, peoSkills))
