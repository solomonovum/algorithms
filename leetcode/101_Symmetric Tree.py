# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        nodes = [root]

        left_list = self.traverse([nodes[0].left])
        right_list = self.traverse([nodes[0].right], False)

        if left_list == right_list:
            return True
        else:
            return False

    def traverse(self, nodes, left_start=True):
        res = []
        while nodes:
            for node in nodes:
                if node:
                    res.append([node.val])
                else:
                    res.append(None)
            if left_start:
                nodes = [x for node in nodes if node for x in (node.left, node.right)]
            else:
                nodes = [x for node in nodes if node for x in (node.right, node.left)]
        return res
