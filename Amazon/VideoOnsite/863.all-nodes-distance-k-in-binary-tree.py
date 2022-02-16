#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convert_into_graph(self, node, parent, g):
        if not node:
            return
        if parent:
            g[node].append(parent)

        if node.right:
            g[node].append(node.right)
            self.convert_into_graph(node.right, node, g)
        if node.left:
            g[node].append(node.left)
            self.convert_into_graph(node.left, node, g)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        g = collections.defaultdict(list)
        vis, q, res = set(), collections.deque(), []
        self.convert_into_graph(root, None, g)

        q.append((target, 0))

        while q:
            n, d = q.popleft()
            vis.add(n)
            if d == k:
                res.append(n.val)

            for nb in g[n]:
                if nb not in vis:
                    q.append((nb, d + 1))
        return res

# @lc code=end
