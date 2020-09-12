#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #def reverseList(self, head: ListNode) -> ListNode:
    #    if not head or not head.next:
    #        return head
    #    prev = None
    #    cur = head
    #    while cur:
    #        nxt = cur.next
    #        cur.next = prev
    #        prev = cur
    #        cur = nxt
    #    return prev

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead

# @lc code=end
