from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head
        tail.before = None
        len = 1
        while tail.next != None:
            tail.next.before = tail
            tail = tail.next
            len += 1
        print(tail.val)
        
        left, right = head, tail
        for i in range(len//2):
            if not left.val == right.val:
                return False
            left = left.next
            right = right.before
            
    