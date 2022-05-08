# Definition for singly-linked list.
from typing import Optional, List

# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = node = ListNode()
        lists = [x for x in lists if x]
        while lists:
            min_node_index = lists.index(min(lists, key=lambda x: x.val))
            node.next = lists[min_node_index]
            node = node.next
            if lists[min_node_index].next == None:
                lists.pop(min_node_index)
            else:
                lists[min_node_index] = lists[min_node_index].next
        return root.next