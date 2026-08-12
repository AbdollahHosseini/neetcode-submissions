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
            return [root.val] + self.preOrder(root.left) + self.preOrder(root.right) 



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootOrder = self.preOrder(root)
        subOrder = self.preOrder(subRoot)

        for i, val in enumerate(rootOrder):
            r1 = i
            r2 = i
            p1 = 0
            p2 = 1
            if val == subRoot.val:
                r1 = (r1 * 2) + 1
                r2 = (r1 * 2) + 2
                p1 += 1
                p2 += 1
                




        

       


