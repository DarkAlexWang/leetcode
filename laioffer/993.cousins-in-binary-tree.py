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
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False
        q = deque([root])

        while q:
            curlayer = []
            dic = {}
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    dic[cur.left.val] = cur.value
                if cur.right:
                    q.append(cur.right)
                    dic[cur.right.val] = cur.value
                curlayer.append(cur.val)
            if x in curlayer and y in curlayer and dic[x] != dic[y]
                return True
            return False


# @lc code=end
