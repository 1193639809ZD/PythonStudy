from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(left, right):
            # 两个节点都为空
            if not left and not right:
                return True
            # 两个节点中有一个为空
            if not left or not right:
                return False
            # 两个节点的值不相等
            if left.val != right.val:
                return False
            # 用递归函数，比较左节点，右节点是否对称
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
