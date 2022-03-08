import json


class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        tree_lst = {}
        def recur(index, node):
            if node:
                tree_lst[index] = node.val
                recur(2*index+1, node.left)
                recur(2*index+2, node.right)
        recur(0, root)
        return json.dumps(tree_lst)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        data =json.loads(data)
        d = {int(i):j for (i,j) in data.items()}
        def recur(idx:int, node: TreeNode):
            if 2*idx+1 in d:
                node.left = TreeNode(d[2*idx+1])
                recur(2 * idx+1, node.left)
            if 2*idx+2 in d:
                node.right = TreeNode(d[2*idx+2])
                recur(2*idx+2, node.right)
            
        root = TreeNode(d[0])
        recur(0, root)
        return root
