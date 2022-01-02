#
# @lc app=leetcode id=1120 lang=python3
#
# [1120] Maximum Average Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.res = 0

        def dfs(cur):
            # if the tree is emply, then node number and count both are 0
            if cur == None:
                return [0, 0]
            left = dfs(cur.left)
            right = dfs(cur.right)
            count = left[0] + right[0] + 1
            sum_ = left[1] + right[1] + cur.val

            # inumerate cur is the root all the cases, and update the res
            self.res = max(self.res, sum_ / count)
            return [count, sum_]

        dfs(root)
        return self.res




# @lc code=end
