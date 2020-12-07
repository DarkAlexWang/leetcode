#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return -sys.maxsize
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        self.res = max(self.res, root.val + l + r)
        return root.val + max(l, r)

    def maxPathSum(self, root):
        self.res = -sys.maxsize
        self._maxPathSum(root)
        return self.res
# @lc code=end
