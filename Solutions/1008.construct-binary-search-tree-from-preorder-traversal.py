#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        start, end = 0, len(preorder)
        return self.helper(preorder, 0, end)
    def helper(self, preorder, start, end):
        if start >= end:
            return
        node = TreeNode(preorder[start])
        splitNum = start
        while splitNum < end and preorder[splitNum] <= preorder[start]:
            splitNum += 1
        node.left = self.helper(preorder, start + 1, splitNum)
        node.right = self.helper(preorder, splitNum, end)
        return node
# @lc code=end
