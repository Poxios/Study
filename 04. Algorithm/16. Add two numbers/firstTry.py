from typing import Optional

# 2 4 3
# 5 6 4
# -----
# 7 0 8

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = node = ListNode()
        while l1 or l2:
            if ((l1 and l1.next) or (l2 and l2.next)) and not node.next:
                node.next = ListNode()
            if not l1:
                node.val += l2.val
                l2 = l2.next
            elif not l2:
                node.val += l1.val
                l1 = l1.next
            else:
                node.val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            
            if node.val >= 10:
                node.val -= 10
                node.next = ListNode(1)
            node = node.next

        return start
