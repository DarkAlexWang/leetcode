class Solution:
    def count(self, arr):
        if len(arr) == 0:
            return 0
        leftSum = 0
        rightSum = 0
        count = 0

        for i in arr:
            leftSum += i

        for i in range(len(arr) - 1, -1, -1):
            rightSum += arr[i]
            leftSum -= arr[i]

            if rightSum < leftSum and (rightSum != 0 and leftSum != 0):
                count += 1

        return count

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.count([10, 4, -8, 7])
    ans2 = solution.count([10, -4, -2, 10])
    print(ans1)
    print(ans2)
