#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ## recursively
       # res = []
       # self.helper(root, res)
       # return res
    #def helper(self, root, res):
       # if root:
       #     self.helper(root.left, res)
       #     res.append(root.val)
       #     self.helper(root.right, res)
       #
       #
       ## iteratively
        res = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res


# @lc code=end
