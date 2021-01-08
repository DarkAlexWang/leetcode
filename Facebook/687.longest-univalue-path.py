# @lc lang=python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        if root is None:
            return 0
        self.univaluepath(root)
        return self.res
    def univaluepath(self, root):
        if root is None:
            return 0
        l = self.univaluepath(root.left)
        r = self.univaluepath(root.right)
        pl = 0
        pr = 0
        if root.left and root.val == root.left.val:
            pl = l + 1
        if root.right and root.val == root.right.val:
            pr = r + 1
        self.res = max(self.res, pl + pr)
        return max(pl, pr)
