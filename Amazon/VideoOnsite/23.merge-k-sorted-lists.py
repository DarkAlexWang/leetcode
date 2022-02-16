#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)

        while heap:
            val,i, node = heap[0]
            if not node.next:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next

# @lc code=end
