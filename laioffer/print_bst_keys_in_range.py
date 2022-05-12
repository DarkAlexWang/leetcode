class Solution:
    def getRange(self, root, min_, max_):
        if root is None:
            return
        res = []
        if min_ < root.val:
            self.getRange(root.left, min_, max_)
        if min_ <= root.val and max_ >= root.val:
            res.append(root.val)
        self.getRange(root.right, min_, max_)
