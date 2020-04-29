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
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        self.dfs(root)
        return self.ans
    def dfs(self, root):
        if not root:
            return -sys.maxsize
        l = max(0, self.dfs(root.left))
        r = max(0, self.dfs(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)
# @lc code=end
