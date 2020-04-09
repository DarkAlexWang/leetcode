#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        self.dfs(root, sum, [], ans)
        return ans
    def dfs(self, root, sum, temp, ans):
        if not root:
            return
        if root.left == None and root.right == None and sum == root.val:
            ans.append(temp+[root.val])
            return
        self.dfs(root.left, sum-root.val, temp+[root.val], ans)
        self.dfs(root.right, sum-root.val, temp+[root.val], ans)
# @lc code=end
