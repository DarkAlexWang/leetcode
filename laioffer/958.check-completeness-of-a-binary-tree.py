#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = deque([root])
        flag = False
        while q:
            cur = q.popleft()

            if flag:
                if cur.left or cur.right:
                    return False
                continue
            if cur.left and cur.right:
                q.append(cur.left)
                q.append(cur.right)
            elif cur.right:
                return False
            elif cur.left:
                q.append(cur.left)
                flag = True
            else:
                 flag = True
        return True


# @lc code=end
