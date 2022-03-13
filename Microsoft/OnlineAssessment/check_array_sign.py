class Solution:
    def check_array_sign(self, arr):
        res = 1
        for elem in arr:
            res *= elem
        if res < 0:
            return -1
        elif res == 0:
            return 0
        else:
            return 1

if __name__ == "__main__":
    solution = Solution()
    ans = solution.check_array_sign([1, -2, 3, 8, 5])
    print(ans)
