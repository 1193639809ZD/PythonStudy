# @Author: eveleaf
# @Date: 2024-09-09 15:29
# @LastEditTime: 2024-09-09 15:29
# @Description: 链表操作，子链

from typing import Optional
from time import sleep


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)

        sc, lc = small, large

        while head is not None:
            print(head.val)
            # sleep(1)
            if head.val < x:
                sc.next = head
                sc = sc.next
            else:
                lc.next = head
                lc = lc.next
            head = head.next

        # 切断lc.next指针，否则会形成环路
        sc.next = large.next
        lc.next = None
        return small.next


if __name__ == "__main__":
    nums = [1, 4, 3, 2, 5, 2]
    dummy = ListNode(0)
    cur = dummy
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = cur.next

    sol = Solution()

    ans = sol.partition(dummy.next, 3)
    print("结果：")
    while ans is not None:
        print(ans.val)
        # sleep(0.1)
        ans = ans.next
