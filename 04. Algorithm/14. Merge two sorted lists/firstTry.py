from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        head = None
        if not node1 and not node2:
            return None
        if not node1:
            return list2
        if not node2:
            return list1
        
        if node1.val < node2.val:
            head = ListNode(node1.val)
            node1 = node1.next
        else:
            head = ListNode(node2.val)
            node2 = node2.next
        start = head
        while node1 or node2:
            if not node1:
                head.next = ListNode(node2.val)
                node2 = node2.next
            elif not node2 or node1.val < node2.val:
                head.next = ListNode(node1.val)
                node1 = node1.next
            else:
                head.next = ListNode(node2.val)
                node2 = node2.next
            head = head.next
        
        return start