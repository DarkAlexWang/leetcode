#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def label_to_position(label):
            r, c = divmod(label - 1, n)
            if r % 2 == 0:
                return n - 1- r, c
            else:
                return n - 1 - r, n - 1 - c

        visited = set()
        q = collections.deque([])
        q.append((1, 0))
        while q:
            curr_square, step_num = q.popleft()
            r, c = label_to_position(curr_square)
            if board[r][c] != -1:
                curr_square = board[r][c]

            if curr_square == n * n:
                return step_num

            for new_square in range(curr_square + 1, min(curr_square + 6, n * n) + 1):
                if new_square not in visited:
                    visited.add(new_square)
                    q.append((new_square, step_num + 1))
        return -1


# @lc code=end
