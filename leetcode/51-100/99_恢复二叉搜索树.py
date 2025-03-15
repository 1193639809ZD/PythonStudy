# @Author: eveleaf
# @Date: 2024-09-09 17:58
# @LastEditTime: 2024-09-09 17:59
# @Description:

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 中序遍历二叉树，并将遍历的结果保存到list中
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        # 装入列表，好访问
        nodes = []
        dfs(root)
        first = None
        second = None
        pre = nodes[0]
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1, len(nodes)):
            if pre.val > nodes[i].val:
                second = nodes[i]
                if not first:
                    first = pre
            pre = nodes[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
        if first and second:
            first.val, second.val = second.val, first.val
