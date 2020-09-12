class Solution:
    def getrange(self, root, min_value, max_value):
        res = []
        self.helper(root, min_value, max_value, res)
        return res

    def helper(self, root, min_value, max_value, res):
        if root == None:
            return
        if root.val > min_value:
            self.helper(root.left, min_value, max_value, res)
        if root.val >= min_value and root.val <= max_value
            res.append(root.val)
        if root.val < max_value:
            self.helper(root.right, min_value, max_value, res)
