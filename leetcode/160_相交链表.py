from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first, second = headA, headB
        countA = countB = 0
        # 计算A、B链表长度
        while first:
            first = first.next
            countA += 1
        while second:
            second = second.next
            countB += 1
        # first指针指向长链表，并先走abs(countA - countB)步，让first和second可以同时到链表终点
        if countA > countB:
            first, second = headA, headB
        else:
            first, second = headB, headA
        for i in range(abs(countA - countB)):
            first = first.next
        # 节点相同的条件是地址相同
        while first != second:
            first = first.next
            second = second.next
        return first

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     """
    #     思路：表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。则当两链表走到相等的位置时：
    #     x1+y+x2 = x2+y+x1
    #     :param headA:
    #     :param headB:
    #     :return:
    #     """
    #     a = headA
    #     b = headB
    #     while a != b:
    #         a = a.next if a else headB
    #         b = b.next if b else headA
    #     return a
