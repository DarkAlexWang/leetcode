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
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            inpair = self.isMirror(left.right, right.left)
            outpair = self.isMirror(left.left, right.right)
            return outpair and inpair
        else:
            return False
# @lc code=end
