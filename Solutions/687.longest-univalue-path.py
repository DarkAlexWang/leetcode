#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        if root is None:
            return 0
        self.uniValuePath(root)
        return self.ans
    def uniValuePath(self, root):
        if root is None:
            return 0
        l = self.uniValuePath(root.left)
        r = self.uniValuePath(root.right)
        pl = 0
        pr = 0
        if root.left is not None and root.val == root.left.val:
            pl = l + 1
        if root.right is not None and root.val == root.right.val:
            pr = r + 1
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)
# @lc code=end
