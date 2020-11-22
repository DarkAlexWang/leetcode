##Write a function drawHTree that constructs an H-tree, given its center (x and
##y coordinates), a starting length, and depth. Assume that the starting line
##is parallel to the X-axis.  Use the function drawLine provided to implement
##your algorithm. In a production code, a drawLine function would render a real
##line between two points. However, this is not a real production environment,
##so to make things easier, implement drawLine such that it simply prints its
##arguments (the print format is left to your discretion).  Analyze the time
##and space complexity of your algorithm. In your analysis, assume that
##drawLine's time and space complexities are constant, i.e. O(1).


import math
class Solution:
    def drawHTree(self, x, y, length, depth):
        if depth < 1:
            return

        leftx = x - length //2
        lefty = y
        rightx = x + length //2
        righty = y
        uppery = y + length //2
        lowery = y - length // 2
        self.drawLine(leftx, lefty, rightx, lefty)
        self.drawLine(leftx, uppery, leftx, lowery)
        self.drawLine(rightx, uppery, rightx, lowery)
        self.drawHTree(leftx, uppery, length/math.sqrt(2), depth - 1)
        self.drawHTree(rightx, uppery, length/math.sqrt(2), depth - 1)
        self.drawHTree(leftx, lowery, length/math.sqrt(2), depth - 1)
        self.drawHTree(rightx, lowery, length/math.sqrt(2), depth - 1)

    def drawLine(self, leftx, lefty, rightx, righty):
        return

if __name__ == '__main__':
    solution = Solution()
    solution.drawHTree(0, 0, 4, 1)
