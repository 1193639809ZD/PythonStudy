# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 写成属性，可以全局访问
        self.ans = 0

        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            ld = depth(node.left)
            # 右儿子为根的子树的深度
            rd = depth(node.right)
            # 计算每个子树的直径，并跟新结果
            self.ans = max(self.ans, ld + rd)
            # 返回该节点为根的子树的深度
            return max(ld, rd) + 1

        depth(root)
        return self.ans
