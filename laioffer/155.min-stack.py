#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
import collections
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque()
        self.minstack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            if self.minstack[-1] >= x:
                self.minstack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        res = self.stack.pop()
        if self.minstack[-1] == res:
            self.minstack.pop()
        return res

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
