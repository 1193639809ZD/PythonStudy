from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 把节点装入集合(哈希表)，索引比较快
        hash_list = set()
        while head:
            # 如果next节点已经在集合内，则表示有环路
            if head in hash_list:
                return True
            hash_list.add(head)
            head = head.next
        return False

    # 快慢指针
    def fs_nodel_hasCycle(self, head: ListNode) -> bool:
        """使用快慢指针

        Args:
            head (ListNode): 节点列表

        Returns:
            bool: 是否存在环路
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
