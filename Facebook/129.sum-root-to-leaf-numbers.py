#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        queue = collections.deque()
        if root:
            queue.append(root)

        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val * 10
                queue.append(node.left)
            if node.right :
                node.right.val += node.val * 10
                queue.append(node.right)
        return res

# @lc code=end
