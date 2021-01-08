# @lc lang=python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        start, end = 0, len(preorder)
        return self.helper(preorder, start, end)

    def helper(self, preorder, start, end):
        splitNum = start
        if start >= end:
            return
        node = TreeNode(preorder[splitNum])
        while splitNum < end and preorder[splitNum] <= preorder[start]:
            splitNum += 1
        node.left = self.helper(preorder, start + 1, splitNum)
        node.right = self.helper(preorder, splitNum, end)
        return node
