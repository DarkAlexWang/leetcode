# @lc lang=python3
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
        q = collections.deque([root])
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
                flag = True
                q.append(cur.left)
            else:
                flag = True
        return True
