# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Need to know - to serialize, use bfs (low time complexity)
    def serialize(self, root: TreeNode) -> str:
        pass

    def deserialize(self, data: str) -> TreeNode:
        # deserialize with bfs - index of str and index of TreeNode must go together
        pass
        
