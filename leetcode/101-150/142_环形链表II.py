from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 把节点装入集合(哈希表)，索引比较快
        hash_list = set()
        while head:
            hash_list.add(head)
            head = head.next
            # 如果next节点已经在集合内，则表示有环路
            if head in hash_list:
                return head
        return head

    # 快慢指针
    def fs_node_detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化为同一个节点，保证步数满足等式
        slow, fast = head, head
        while True:
            # 如果此时fast到头了，说明没环
            if not fast or not fast.next:
                return None
            # 先走在判断，避免把开头当相遇
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
