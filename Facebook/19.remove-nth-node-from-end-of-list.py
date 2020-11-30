#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or head is None:
            return
        dummy = ListNode(None)
        dummy.next = head
        cur, pre = dummy, dummy
        for _ in range(n):
            cur = cur.next

        while cur and cur.next:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next
# @lc code=end
