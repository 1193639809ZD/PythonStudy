from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root):
            if root:
                inOrder(root.left)
                ans.append(root.val)
                inOrder(root.right)
            else:
                return

        ans = []
        inOrder(root)

        # 不能有重复
        for i in range(1, len(ans)):
            if ans[i - 1] == ans[i]:
                return False

        ass_list = ans.copy()
        ass_list.sort()
        return ans == ass_list
