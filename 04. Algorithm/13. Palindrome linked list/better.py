from typing import Optional

# head = [1,2,2,1]

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow, fast runner solution
        # make rev list to compare with half-left items
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast, rev, rev.next, slow = fast.next.next, slow, rev, slow.next
        if fast:
            slow=slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True
            
            

s = Solution()
print(s.isPalindrome(ListNode(0,ListNode(1, ListNode(2, ListNode(1,ListNode(0)))))))
