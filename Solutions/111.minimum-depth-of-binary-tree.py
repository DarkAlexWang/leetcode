#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None or root.right is None:
            return self.minDepth(root.left) + self.minDepth(root.right) +1
        return min(self.minDepth(root.left), self.minDepth(root.right)) +1
# @lc code=end
