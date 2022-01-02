class Solution:
    def swapArray(self, array):
        # move all 1 to front
        count1 = 0
        step = 0
        for num in array:
            if num == 0:
                step = step + 1
            else:
                count1 = count1 + step

        # move all 1 to end
        count2 = 0
        step = 0
        for num in array:
            if num == 1:
                step = step + 1
            else:
                count2 = count2 + step

        return min(count1, count2)

if __name__ == "__main__":
    solution = Solution()
    res1 = solution.swapArray([0,0,0,1,1,0])
    print(res1)
    res2 = solution.swapArray([1,1,0, 0])
    print(res2)
    res3 = solution.swapArray([0,1,1,0, 0])
    print(res3)
    res4 = solution.swapArray([0,1,1,1,0,0,1])
    print(res4)
