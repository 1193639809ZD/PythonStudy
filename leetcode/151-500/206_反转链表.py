from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个头节点
        dummy = ListNode()
        # 循环摘除每个节点，并插入到头节点之后
        while head:
            # 取出当前节点，首指针后移
            temp_node = head
            head = head.next
            # 插入到头节点之后
            temp_node.next = dummy.next
            dummy.next = temp_node
        return dummy.next
