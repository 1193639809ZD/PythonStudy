from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # 计算链表长度
        n = 1
        h = head
        while h.next:
            h = h.next
            n += 1
        # 整合成循环链表
        h.next = head
        # 计算偏转量
        k = k % n
        # 抵达偏转位置
        h = res = head
        for i in range(n - k - 1):
            h = h.next
        res = h.next
        h.next = None
        return res
