#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        cur, pre, pre_right = root, None, None
        while cur:
            temp1, temp2 = cur.left, cur.right
            cur.left, cur.right = pre_right, pre
            cur, pre, pre_right = temp1, cur, temp2
        return pre

# @lc code=end
