from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 or root2):
            return
        root = TreeNode()
        def recursive(target, a, b):
            if not a:
                a=TreeNode()
            if not b:
                b=TreeNode()
            target.val += a.val
            target.val += b.val
            if a.left or b.left:
                target.left = TreeNode()
                recursive(target.left, a.left, b.left)
            if a.right or b.right:
                target.right = TreeNode()
                recursive(target.right, a.right, b.right)

        recursive(root,root1,root2)
        return root

