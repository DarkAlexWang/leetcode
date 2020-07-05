#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        d, q, nq = 1, {n}, set()
        while q:
            for node in q:
                for square in squares:
                    if node == square:
                        return d
                    if node < square:
                        break
                    nq.add(node - square)
                    #print('nq =', nq)
                    #print('q', q)
            q, nq, d = nq, set(), d+ 1
            print(q)
        return q
# @lc code=end
