#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # -1 is not balanced
        return self.height(root) != -1

    def height(self, root):
        if root is None:
            return 0
        leftheight = self.height(root.left)
        if leftheight == -1:
            return -1
        rightheight = self.height(root.right)
        if rightheight == -1:
            return -1

        if abs(rightheight - leftheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

# @lc code=end
