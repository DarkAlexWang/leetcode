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
        if root == null:
            return True
        stack = []
        pre = TreeNode(null)
        while root != null and stack is not None:
            while root != null:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre != null and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True

# @lc code=end
