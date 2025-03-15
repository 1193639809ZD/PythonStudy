# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 创建一个首节点，保证之后流程一致
        dummyHead = ListNode(0, head)
        temp = dummyHead
        # 保证下面交换的两个节点存在
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        # 返回头节点
        return dummyHead.next
