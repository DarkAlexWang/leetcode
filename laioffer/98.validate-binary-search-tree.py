#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lowerbound, upperbound):
            if not node:
                return True
            if node.val <= lowerbound or node.val >= upperbound:
                return False
            return dfs(node.right, node.val, upperbound) and dfs(node.left, lowerbound, node.val)
        return dfs(root, float('-inf'), float('inf'))
# @lc code=end
