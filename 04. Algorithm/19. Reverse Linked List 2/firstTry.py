# Definition for singly-linked list.
from inspect import EndOfBlock


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = node = head

        end_of_left = None
        start_of_rev = None

        for _ in range(left - 1):
            end_of_left = node
            node = node.next

        start_of_rev = node
        runner = node.next
        for _ in range(right - left):
            runner.next, runner, node = node, runner.next, runner

        start_of_rev.next = runner
        if end_of_left:
            end_of_left.next = node

        if left == 1:
            start = node

        return start
