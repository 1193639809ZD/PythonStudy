from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 必定存在满足情况的节点
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[
        TreeNode]:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左节点为p、q其中一个的祖先
        if not left:
            return right
        # 右节点为p、q其中一个的祖先
        if not right:
            return left
        # 如果p、q在两侧，则返回root
        return root
