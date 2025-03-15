# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    # 快慢指针
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     # 创建一个首节点，保证删除流程一致
    #     dummy = ListNode(0, head)
    #     # 声明fast、slow指针，fast先走n步
    #     slow, fast = dummy, head
    #     for _ in range(n):
    #         fast = fast.next
    #     # fast和slow一起走，当fast走到最后一个节点的时候，slow下一个节点即是要删除的节点
    #     while fast:
    #         slow, fast = slow.next, fast.next
    #     slow.next = slow.next.next
    #     return dummy.next


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    n = 2
    s = Solution()
    print(s.removeNthFromEnd(head, n))
