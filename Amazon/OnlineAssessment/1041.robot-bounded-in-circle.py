#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0

        # keep track of directions
        d = "N"
        for c in instructions:
            if c == 'G':
                if d == "N":
                    y += 1
                elif d == "E":
                    x += 1
                elif d == 'S':
                    y -= 1
                else:
                    x -= 1
            elif c == 'L':
                if d == "N":
                    d = "W"
                elif d == "E":
                    d = "N"
                elif d == 'S':
                    d = "E"
                else:
                    d = "S"
            else:
                if d == "N":
                    d = "E"
                elif d == "E":
                    d = "S"
                elif d == 'S':
                    d = "W"
                else:
                    d = "N"

        # check if calculated position is starting position
        if x == 0 and y == 0:
            return True
        # check if the final faced direction is not North (starting Direction)
        if d == "N":
            return False
        return True


# @lc code=end
