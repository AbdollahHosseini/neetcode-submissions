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
        arr = [root]
        subOrder = self.preOrder(subRoot)
        while arr:
            curr = arr.pop()
            if curr.val == subRoot.val and (subOrder == self.preOrder(curr)):
                return True

            if curr.left:
                arr.append(curr.left)
            if curr.right:
                arr.append(curr.right)

        return False

        

       


