class Solution:
    def mergesort(self, arry):
        cur, pre = head, ListNode(None)
        while cur and cur.next:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
