#
# @lc app=leetcode id=558 lang=python3
#
# [558] Logical OR of Two Binary Grids Represented as Quad-Trees
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':

# @lc code=end
