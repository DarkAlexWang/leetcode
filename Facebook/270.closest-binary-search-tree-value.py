#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = float('inf')
        def helper(root, value):
            if not root or root is None:
                return
            if abs(root.val - target) < abs(self.closest - target):
                self.closest =  root.val
            if root.val < target:
                helper(root.right, target)
            if root.val > target:
                helper(root.left, target)
        helper(root, target)
        return self.closest
# @lc code=end
