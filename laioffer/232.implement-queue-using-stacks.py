#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input =  []
        self.out = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.out == []:
            while self.input:
                self.out.append(self.input.pop())
        return self.out[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.input)  == 0 and len(self.out) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
