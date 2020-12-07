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
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        conn = collections.defaultdict(list)
        def build_graph(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                build_graph(child, child.left)
            if child.right:
                build_graph(child, child.right)
        build_graph(None, root)

        bfs = [target.val]
        seen = set(bfs)

        for i in range(K):
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            seen |= set(bfs)
        return bfs
# @lc code=end
