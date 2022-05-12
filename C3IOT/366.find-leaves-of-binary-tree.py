#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev].append(root.val)
            return lev
        dic, res = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            res.append(dic[i])
        return res
# @lc code=end
