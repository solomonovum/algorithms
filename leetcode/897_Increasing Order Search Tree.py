# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = []
    ans = node = TreeNode(None)

    def __init__(self):
        self.result.clear()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self._traverse_inorder(root)
        self._make_node()
        return self.ans.right

    def _traverse_inorder(self, nodes):
        if nodes is None:
            return
        self._traverse_inorder(nodes.left)
        self.result.append(nodes.val)
        self._traverse_inorder(nodes.right)

    def _make_node(self):
        for val in self.result:
            self.node.right = TreeNode(val)
            self.node = self.node.right
