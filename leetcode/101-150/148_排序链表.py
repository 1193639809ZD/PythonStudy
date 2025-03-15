from typing import Optional
from functools import cmp_to_key


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ass_list = []
        while head:
            # 只添加值
            ass_list.append(head.val)
            head = head.next
        ass_list.sort()

        if len(ass_list) == 0:
            return

        dummy = ListNode(ass_list[0])
        head = dummy
        for i in range(1, len(ass_list)):
            head.next = ListNode(ass_list[i])
            head = head.next
        return dummy

