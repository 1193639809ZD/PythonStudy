from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # 把节点装入列表，便于根据下标找到对应节点
    #     ass_list = []
    #     while head:
    #         ass_list.append(head)
    #         head = head.next
    #     # 查看节点列表否满足回文条件
    #     for i in range(len(ass_list) // 2):
    #         if ass_list[i].val != ass_list[-(i + 1)].val:
    #             return False
    #     return True

    # 优化：不需要装入节点，只需要装入节点的值即可
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ass_list = []
        while head:
            ass_list.append(head.val)
            head = head.next
        return ass_list == ass_list[::-1]
