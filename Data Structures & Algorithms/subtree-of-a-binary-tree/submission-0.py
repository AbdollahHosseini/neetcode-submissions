# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def preOrder(self, node):
        if not node:
            return []
        else:
            left = self.preOrder(node.left)
            mid = [node.val]
            right = self.preOrder(node.right)
            return left + mid + right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       
        arr = [root]
        while arr:
            curr = arr.pop()
            if curr.val == subRoot.val:
                return (self.preOrder(curr) == self.preOrder(subRoot))
            else:
                if curr.left:
                    arr.append(curr.left)
                if curr.right:
                    arr.append(curr.right)
        
        return False
        

       


