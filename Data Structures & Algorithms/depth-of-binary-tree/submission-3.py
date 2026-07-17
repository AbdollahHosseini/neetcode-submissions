# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # traverse post order

        # if none, return 0 (nothing to count)

        # return max between 1 + left and 1 + right (only ever counts the deeper side)

        def _count_depth(node):

            if not node:
                return 0

            return max(1 + _count_depth(node.left), 1 + _count_depth(node.right))

        return _count_depth(root)


