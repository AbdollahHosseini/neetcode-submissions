# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 0
        Lroot = root
        Rroot = root

        while Lroot:
            left += 1
            Lroot = Lroot.left

        while Rroot:
            right += 1
            Rroot = Rroot.right

        return max(left, right)
