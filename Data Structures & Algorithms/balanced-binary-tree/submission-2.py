class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return (abs(left_height - right_height) <= 1 
                    and self.isBalanced(root.left) 
                    and self.isBalanced(root.right))