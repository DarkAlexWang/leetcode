#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for new in asteroids:
            while res and new < 0 < res[-1]:
                if res[-1] < -new:
                    res.pop()
                    continue
                elif res[-1] == -new:
                    res.pop()
                break
            else:
                res.append(new)
        return res
# @lc code=end
