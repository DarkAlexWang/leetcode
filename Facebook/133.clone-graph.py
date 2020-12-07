#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        dic = {node: Node(node.val)}

        q = collections.deque([node])
        while q:
            cur = q.popleft()
            for nb in cur.neighbors:
                if nb not in dic:
                    dic[nb] = Node(nb.val)
                    q.append(nb)
                dic[cur].neighbors.append(dic[nb])
        return dic[node]

# @lc code=end
