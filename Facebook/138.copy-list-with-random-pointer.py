# @lc app=leetcode id=138 lang=python3
#"""
## Definition for a Node.
#class Node:
#    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#        self.val = int(x)
#        self.next = next
#        self.random = random
#"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pre, node, dic = None, head, {}
        while node:
            if node not in dic:
                dic[node] = Node(node.val, node.next, node.random)
            if pre:
                pre.next = dic[node]
            else:
                head = dic[node]
            if node.random:
                if node.random not in dic:
                    dic[node.random] = Node(node.random.val, node.random.next, node.random.random)
                dic[node].random = dic[node.random]
            node = node.next
            pre = dic[node]
        return head
