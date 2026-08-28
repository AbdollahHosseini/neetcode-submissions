# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode, MAX=float('-inf')) -> int:
        if not root:
            return 0
        if root.val >= MAX:
            MAX = root.val
            return 1 + self.goodNodes(root.left, MAX) + self.goodNodes(root.right, MAX)
        else:
            return self.goodNodes(root.left, MAX) + self.goodNodes(root.right, MAX)