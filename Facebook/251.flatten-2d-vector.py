#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#

# @lc code=start
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.col = 0
        self.row = 0
        self.vec = vec

    def next(self) -> int:
        if self.hasNext():
            result = self.vec[self.row][self.col]
            self.col += 1
            return result


    def hasNext(self) -> bool:
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True
            self.col = 0
            self.row += 1
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
