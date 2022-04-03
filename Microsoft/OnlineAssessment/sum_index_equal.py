class Solution:
    def sum_index_equal(self, A, B):
        sum_A = sum(A)
        sum_B = sum(B)
        if len(A) < len(B):
            A, B = B, A
        i = 0
        while i < len(A):
            sum_left_A = sum(A[:i])
            sum_left_B = sum(B[:i])
            sum_right_A = sum_A - sum_left_A
            sum_right_B = sum_B - sum_left_B
            i += 1
            if sum_left_A == sum_left_B and sum_right_A == sum_right_B:
                return i
            else:
                continue

        return -1

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sum_index_equal([2, 7, -2, 6], [-1, 10, 1, 3])
    print(ans)
