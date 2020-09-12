#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        small = ListNode()
        large = ListNode()
        cursmall = small
        curlarge = large
        while head:
            if head.val < x:
                cursmall.next = head
                cursmall = cursmall.next
            else:
                curlarge.next = head
                curlarge = curlarge.next
            head = head.next

        cursmall.next = large.next
        curlarge.next = None
        return small.next
# @lc code=end
