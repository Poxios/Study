from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        before = head
        node = head = head.next
        isOdd = False
        while node.next:
            if not node.next.next:
                node.next, before.next, node = before, node.next, node.next
                isOdd = True
            else:
                node.next, before.next, node, before = before, node.next.next, node.next.next, node.next
        if not isOdd:
            node.next, before.next = before, None
        return head


s = Solution()
v = s.swapPairs(ListNode(0, ListNode(1, ListNode(1, ListNode(0)))))
print('---------------')
print(v.val)
print(v.next.val)
print(v.next.next.val)
print(v.next.next.next.val)
