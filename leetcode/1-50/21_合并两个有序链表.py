from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # 对两个链表进行排序
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
        # ans指向较小的那个值
        ans = list1 if list1.val < list2.val else list2
        return ans


if __name__ == '__main__':
    print("hello world!")
    list1 = ListNode(1)
    list1.next = ListNode(2)
    ans = 1 if 1 > 2 else 2
    print(ans)
