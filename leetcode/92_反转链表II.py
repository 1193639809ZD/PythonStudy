# @Author: eveleaf
# @Date: 2024-09-09 16:28
# @LastEditTime: 2024-09-09 17:26
# @Description: 反转链表

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        start, end = dummy, head

        for i in range(left - 1):
            start = start.next
            end = end.next

        for i in range(right - left):
            t = end.next
            end.next = t.next
            t.next = start.next
            start.next = t
        for i in range(10 + 1):
            pass
        return dummy.next
