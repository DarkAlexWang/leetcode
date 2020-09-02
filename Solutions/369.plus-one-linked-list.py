#
# @lc app=leetcode id=886 lang=python3
#
# [369] Plus One Linked List
#

# @lc code=start
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head
        rev_head = self.reverse(head)
        curr = rev_head
        pre = curr
        carry = 1
        while curr:
            pre = curr
            tmp = curr.val + carry
            curr.val = tmp % 10
            carry = tmp//10
            if carry == 0:
                break
            curr = curr.next
        if carry:
            pre.next = ListNode(1)
        return self.reverse(rev_head)

    def reverse(self, head):
        if not head:
            return head
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

# @lc code=end
