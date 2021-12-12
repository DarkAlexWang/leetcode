class Node:
    def __init__(self,data, nxt = None):
        self.data = data
        self.next = nxt

def insert(root,val):
    if not root:
        root = Node(val)
    else:
        cur = root
        while cur.next:
            cur = cur.next
        cur.next=Node(val)
    return root
def listToNode(numbers):
    root = None
    for num in numbers:
        root = insert(root,num)
    return root

#####helper funciton don't delete or change
def reverseLinkedList(node):
    prev = None
    while node:
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
    return prev

def maxinumPages(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    new_head = slow.next
    slow.next = None
    rev_head = reverseLinkedList(new_head)
    max_pages = 0
    while head or rev_head:
        if head:
            p1 = head.data
            head = head.next
        else:
            p1 = 0

        if rev_head:
            p2 = rev_head.data
            rev_head = rev_head.next
        else:
            p2 = 0
        max_pages = max(max_pages,p1+p2)

    return max_pages
numbers = [1,4,3,2]
# numbers = [3,1,1,3]
# numbers = [3,1,9,3,3]
head = listToNode(numbers)
print(maxinumPages(head))
