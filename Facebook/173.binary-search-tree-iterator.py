#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.pushAll(root)

    def next(self) -> int:
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val


    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
