from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preOrder(root):
            if root:
                pre_list.append(root)
                preOrder(root.left)
                preOrder(root.right)
            else:
                return

        # 节点数为0，直接返回
        if not root:
            return root

        pre_list = []
        preOrder(root)

        # 串联列表
        n = len(pre_list)
        for i in range(n):
            if i == n - 1:
                return pre_list[0]
            pre_list[i].left = None
            pre_list[i].right = pre_list[i + 1]
