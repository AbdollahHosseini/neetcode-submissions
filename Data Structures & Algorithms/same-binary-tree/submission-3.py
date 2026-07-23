# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root):
        if not root:
            return [None]
        else:
            left = self.inOrder(root.left)
            mid = [root.val]
            right = self.inOrder(root.right)
            return mid + left + right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        x = self.inOrder(p)
        y = self.inOrder(q)

        if x == y:
            return True
        else: return False