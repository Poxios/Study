# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left) # max depth of left
            right = dfs(node.right) # max depth of right

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1 # return depth

        dfs(root)
        return self.longest