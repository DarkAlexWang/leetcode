# @lc lang=python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        x_nodes_dic = collections.defaultdict(list)
        self.dfs(root, 0, 0, x_nodes_dic)

        result = []
        for k in sorted(x_nodes_dic):
            level = [item[1] for item in sorted(x_nodes_dic[k], key = lambda x: (x[0], x[1]))]
            result.append(level)
        return result
    def dfs(self, root, x, y, x_nodes_dic):
        if root is None:
            return
        x_nodes_dic[x].append((y, root.val))
        self.dfs(root.left, x- 1, y + 1, x_nodes_dic)
        self.dfs(root.right, x + 1, y + 1, x_nodes_dic)
