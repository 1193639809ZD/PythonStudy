from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序根节点索引，中序遍历的左边界和右边界
        def in_pre_build(root, left, right):
            # 递归终止
            if left > right:
                return
                # 建立根节点
            node = TreeNode(preorder[root])
            # 划分根节点、左子树、右子树
            root_index = ass_dict[preorder[root]]
            # 开启左子树递归
            node.left = in_pre_build(root + 1, left, root_index - 1)
            # 开启右子树递归
            node.right = in_pre_build(root_index - left + root + 1, root_index + 1, right)
            # 回溯返回根节点
            return node

        # 创建一个hash表存储中序列表，加速索引
        ass_dict = {element: i for i, element in enumerate(inorder)}
        return in_pre_build(0, 0, len(inorder) - 1)

    # 递归
    # def buildTree(self, preorder, inorder):
    #     if inorder:
    #         index = inorder.index(preorder[0])
    #         root = TreeNode(inorder[index])
    #         root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
    #         root.right = self.buildTree(preorder[index + 1 :], inorder[index + 1 :])
    #         return root
