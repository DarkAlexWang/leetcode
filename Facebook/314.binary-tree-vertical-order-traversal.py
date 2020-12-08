#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        treemap = collections.defaultdict(list)
        q = collections.deque([(0, root)])
        while q:
            pos, node = q.popleft()
            treemap[pos].append(node.val)
            if node.left:
                q.append((pos - 1, node.left))
            if node.right:
                q.append((pos + 1, node.right))
        for i in sorted(treemap):
            res.append(treemap[i])
        return res
# @lc code=end
