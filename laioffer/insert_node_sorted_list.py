class Solution:
    def insert(self, head, value):
        node = ListNode()
        if head is None:
            node.val = value
            node.next = head
            head = node
        elif head.val >= value:
            node.next = head
            head = node
        else:
            cur = head
            while cur.next is not None and cur.next.val < value:
                cur = cur.next
            node.next = cur.next
            cur.next = node
