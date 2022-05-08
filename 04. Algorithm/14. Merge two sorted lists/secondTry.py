from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = result = ListNode()
        while list1 or list2:
            if not list1 or list2 and list1.val > list2.val:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next
            result = result.next
        return start.next