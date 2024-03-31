from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = head = ListNode()
        # 两个节点有一个有值，都继续相加
        while l1 or l2:
            # 哪个链表用完了则用0补上
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            # 个位数的结果
            sum = (l1.val + l2.val + carry) % 10
            # 十位数的结果
            carry = (l1.val + l2.val + carry) // 10

            cur.next = ListNode(sum)
            cur = cur.next

            l1 = l1.next
            l2 = l2.next

        # 如果十位数多进位了，则新建一个节点
        if carry != 0:
            cur.next = ListNode(val=carry)

        return head.next


if __name__ == '__main__':
    print("hello")
