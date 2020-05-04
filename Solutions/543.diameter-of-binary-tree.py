#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.LP(root)
        return self.ans
    def LP(self, root):
        if root is None:
            return -1
        l = self.LP(root.left) + 1
        r = self.LP(root.right) + 1
        self.ans = max(self.ans, l + r)
        return max(l, r)
# @lc code=end
