#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy
    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])





# @lc code=end
