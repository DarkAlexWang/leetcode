#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, 0, len(preorder) -1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, pleft, pright, inorder, ileft, iright):
        if pleft > pright or ileft > iright:
            return None
        for i in range(ileft, iright+1):
            if preorder[pleft] == inorder[i]:
                break
        cur = TreeNode(preorder[pleft])
        cur.left = self.helper(preorder, pleft + 1, pleft +i -ileft, inorder, ileft, i-1)
        cur.right = self.helper(preorder, pleft +i -ileft + 1, pright, inorder, i+ 1,  iright)
        return cur

# @lc code=end
