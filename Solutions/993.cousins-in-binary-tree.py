#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xParent = TreeNode(None)
        self.yParent = TreeNode(None)
        self.xDepth, self.yDepth = -1, -2
        self.dfs(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent
    def dfs(self, root, parent, x, y, depth):
        if root == None:
            return
        if x == root.val:
            self.xParent = parent
            self.xDepth = depth
        elif y == root.val:
            self.yParent = parent
            self.yDepth = depth
        else:
            self.dfs(root.left, root, x, y, depth+1)
            self.dfs(root.right, root, x, y, depth+1)
# @lc code=end
