#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ## recursively
        #if not root:
        #    return []
        #res = []
        #self.helper(root, res)
        #return res
    #def #helper(self, root, res):
        #if root:
        #    self.helper(root.left, res)
        #    self.helper(root.right, res)
        #    res.append(root.val)
        ## iteratively preorder reverse
        if not root:
            return None
        res, stack = [], []
        stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]

        ## iteratively postorder



# @lc code=end
