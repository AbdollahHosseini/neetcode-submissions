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
        prev = res[0]

        for i in range(1, len(res)):
            if prev >= res[i]:
                return False
            else: prev = res[i]

        print(res)

        return True
        