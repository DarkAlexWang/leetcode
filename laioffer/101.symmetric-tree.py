#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checksym(root.left, root.right)
    def checksym(self, one, two):
        if one is None and two is None:
            return True
        elif one is None or two is None:
            return False
        elif one.val != two.val:
            return False
        return self.checksym(one.left, two.right) and self.checksym(one.right, two.left)
# @lc code=end
