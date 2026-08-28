# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recurs(self, root, MAX):
        if not root:
            return 0
        if root.val >= MAX:
            MAX = root.val
            return 1 + self.recurs(root.left, MAX) + self.recurs(root.right, MAX)
        else:
            return self.recurs(root.left, MAX) + self.recurs(root.right, MAX)

    def goodNodes(self, root: TreeNode) -> int:
        
        return self.recurs(root, root.val)
        