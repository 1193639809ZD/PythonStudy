from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前缀和
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            # 计算当前前缀和
            curr += root.val
            # 查询是否有满足条件的路径
            ret += prefix[curr - targetSum]
            # 更新哈希表
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            # 注意：不能包含子结点到父节点，因此返回的时候要把当前节点的前缀和剪掉
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)

    # 递归
    # def pathSum(self, root: TreeNode, targetSum: int) -> int:
    #     def rootSum(root, targetSum):
    #         if root is None:
    #             return 0
    #
    #         ret = 0
    #         if root.val == targetSum:
    #             ret += 1
    #
    #         ret += rootSum(root.left, targetSum - root.val)
    #         ret += rootSum(root.right, targetSum - root.val)
    #         return ret
    #
    #     if root is None:
    #         return 0
    #
    #     ret = rootSum(root, targetSum)
    #     ret += self.pathSum(root.left, targetSum)
    #     ret += self.pathSum(root.right, targetSum)
    #     return ret
