# @Author: eveleaf
# @Date: 2024-09-04 20:11
# @LastEditTime: 2024-09-04 20:11
# @Description:

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            cur = head
        else:
            return head

        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
