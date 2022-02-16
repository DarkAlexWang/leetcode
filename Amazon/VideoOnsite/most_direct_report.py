"""
Given a company Organization chart, return the one with most direct reports.
Here ans is MGR1 with 4 direct reportees.
CEO
/ \
VP1 VP2 VP3
/
MGR1
/ / \
EMP4 EMP1 EMP2 EMP3
"""
class TreeNode(object):
    def __init__(self, s, children):
        self.s = s
        self.children = children


class Solution(object):
    def traversal(self, root, res):
        if root is None or root.children is None:
            return
        if res is None or len(res.children) < len(root.children):
            res = root
        for child in root.children:
            self.traversal(child, res)
        return res
        """
        q = collections.deque()
        q.append(arr)
        max_level = 0
        while q:
            size = len(q)
            max_level = max(max_level, size)
            while size > 0:
                current = q.popleft()
                for child in current.children:
                    q.append(child)
        return max_level
        """

    def organizationChart(self, root):
        if root is None:
            return root
        res = root
        ans = self.traversal(root, res)
        return ans

if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(None, None)
    root.s = 'CEO'
    node1 = TreeNode(None, None)
    node2 = TreeNode(None, None)
    node3 = TreeNode(None, None)
    node1.s = 'VP1'
    node2.s = 'VP2'
    node3.s = 'VP3'
    root.children = [node1, node2, node3]
    node4 = TreeNode(None, None)
    node5 = TreeNode(None, None)
    node6 = TreeNode(None, None)
    node7 = TreeNode(None, None)
    node8 = TreeNode(None, None)
    node4.s = 'MGR1'
    node1.children = [node4]
    node5.s = 'EMP4'
    node6.s = 'EMP1'
    node7.s = 'EMP2'
    node8.s = 'EMP3'
    node4.children = [node5, node6, node7, node8]
    ans1 = solution.organizationChart(root)
    print(ans1.s)
