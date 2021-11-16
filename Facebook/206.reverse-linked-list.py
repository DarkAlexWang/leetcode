#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, cur = None, head
        while head:
            cur = head
            head = head.next
            cur.next = dummy
            dummy = cur
        return dummy

# @lc code=end
