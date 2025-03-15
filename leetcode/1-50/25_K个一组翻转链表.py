from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 反转链表，并返回头、尾节点
        def reverseList(reverse_head: Optional[ListNode]):
            dummy = ListNode(0)
            tail = reverse_head
            while reverse_head:
                temp_node = reverse_head
                reverse_head = reverse_head.next
                temp_node.next = dummy.next
                dummy.next = temp_node
            return dummy.next, tail

        # 剩余链表长度是否足够
        def flag(interval_head, k):
            count = 0
            while interval_head:
                count += 1
                interval_head = interval_head.next
                if count == k:
                    return True
            return False

        dummy = ListNode(0, head)
        # 每段链表范围为(start.next, ptr)，注意反转前断开链表，反转后再连接
        start, ptr, end = dummy, dummy, head
        while True:
            if flag(start.next, k):
                for i in range(k):
                    ptr = ptr.next
                    end = end.next
                ptr.next = None
                start.next, ptr = reverseList(start.next)
                # 更新指针
                start = ptr
                ptr.next = end
            else:
                break

        return dummy.next
