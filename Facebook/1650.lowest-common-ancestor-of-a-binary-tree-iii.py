#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #p1, p2 = p, q
        #while p1 != p2:
        #    p1 = p1.parent if p1.parent else q
        #    p2 = p2.parent if p2.parent else p
        #return p1
        visited = set()
        while p:
            visited.add(p.val)
            p = p.parent
        while q:
            if q.val in visited:
                return q
            visited.add(q.val)
            q = q.parent
        return None
# @lc code=end
