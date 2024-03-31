from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for nodeList in lists:
            while nodeList:
                ans.append(nodeList.val)
                nodeList = nodeList.next
        if len(ans) == 0:
            return

        ans.sort()
        dummy = ListNode(ans[0])
        head = dummy
        for i in range(1, len(ans)):
            head.next = ListNode(ans[i])
            head = head.next
        return dummy
