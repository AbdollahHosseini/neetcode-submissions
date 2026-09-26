# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]

        prevLeft = None
        left = root.left
        right = root.right

        while right:
            res.append(right.val)

            if left:
                if left.right:
                    left = left.right
                else:
                    left = left.left

            if right.right:
                right = right.right
            else:
                right = right.left

        while left:
            res.append(left.val)

            if left.right:
                left = left.right
            else:
                left = left.left

        return res



         




