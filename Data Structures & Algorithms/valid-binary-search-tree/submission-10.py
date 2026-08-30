# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def boundary(self, root, lower, upper):
        if not root:
            return True
        elif root.val >= upper or root.val <= lower:
            return False
        else:
            return self.boundary(root.left, lower, root.val) and self.boundary(root.right, root.val, upper)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.boundary(root.left, float('-inf'), root.val) and self.boundary(root.right, root.val, float('inf')) 

        