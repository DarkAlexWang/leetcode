#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        cur = root
        nxt = root.left
        while cur.left:
             cur.left.next = cur.right
             if cur.next:
                 cur.right.next = cur.next.left
                 cur = cur.next
             else:
                 cur = nxt
                 nxt = nxt.left
        return root
# @lc code=end
