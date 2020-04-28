# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1, seq2 = [], []
        self._inorderTraverse(root1, seq1, root1.val)
        self._inorderTraverse(root2, seq2, root2.val)

        if seq1 == seq2:
            return True
        else:
            return False

    def _inorderTraverse(self, node, seq, val):
        # exit condition
        if node is None:
            seq.append(val)
            return

        # in-order traversing
        self._inorderTraverse(node.left, seq, node.val)
        if node.left is None and node.right:
            del seq[-1]
        if node.right is None:
            return
        self._inorderTraverse(node.right, seq, node.val)
