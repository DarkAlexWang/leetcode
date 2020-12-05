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
        def dfs(root, lowerbound, upperbound):
            if not root:
                return True
            if root.val <= lowerbound or root.val >= upperbound:
                return False
            else:
                return dfs(root.left, lowerbound, root.val) and dfs(root.right, root.val, upperbound)
        return dfs(root, -sys.maxsize, sys.maxsize)


# @lc code=end
