# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        
        # set sum
        self.sum = sum
        self.key = False

        # exception handling
        if root.left is None and root.right is None and root.val is self.sum:
            return True
        
        self.dfs(root, 0)

        return self.key

    def dfs(self, nodes, sum):
        # exit condition
        if self.key: return

        if nodes is None: return

        sum += nodes.val

        if sum == self.sum and (nodes.left is None and nodes.right is None):
            self.key = True

        self.dfs(nodes.left, sum)
        self.dfs(nodes.right, sum)
