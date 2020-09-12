#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head
        mid = self.middlenode(head)
        one = head
        two = mid.next
        mid.next = None
        return self.merge(one, self.reverse(two))

    def middlenode(self, head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if head == None or head.next == None:
            return head
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def merge(self, one, two):
        dummy = ListNode()
        cur = dummy
        while one is not None and two is not None:
            cur.next = one
            one = one.next
            cur.next.next = two
            two = two.next
            cur = cur.next.next
        if one is not None:
            cur.next = one
        else:
            cur.next = two

        return dummy.next


# @lc code=end
