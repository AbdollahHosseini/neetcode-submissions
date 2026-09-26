# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preOrder(self, root):
        if not root:
            return []
        else:
            return self.preOrder(root.left) + [root.val] + self.preOrder(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = self.preOrder(root)
        
        p = 0

        while p < len(res):
            if res[p] > res[p + 1]:
                return False

        return True
        