# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    longest = 0
    cur_num = None
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            # no idea