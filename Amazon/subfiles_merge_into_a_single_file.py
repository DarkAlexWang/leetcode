class Solution:
    def cost(self, n, arr):
        if n < 2:
            return 0
        arr.sort()
        res = 0
        prevSum = arr[0]
        for i in range(1, len(arr)):
            prevSum += arr[i]
            res += prevSum
        return res

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.cost(4, [4, 8, 6, 12])
    print(ans1)
