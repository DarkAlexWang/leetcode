# @lc lang=python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return -1
        l = self.helper(root.left) + 1
        r = self.helper(root.right) + 1
        self.res = max(self.res, l + r)
        return max(l, r)
