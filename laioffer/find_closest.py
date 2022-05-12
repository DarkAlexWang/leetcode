class Solution:
    def findClosest(self, nums, target):
        if target <= nums[0]:
            return nums[0]
        if target >= nums[-1]:
            return nums[-1]
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return  nums[mid]
            if target < nums[mid]:
                if mid > 0 and target > nums[mid - 1]:
                    return self.getClosest(nums[mid - 1], nums[mid], target)
                j = mid
            else:
                if mid < len(nums) - 1 and target < nums[mid + 1]:
                    return self.getClosest(nums[mid], nums[mid + 1], target)
                i = mid + 1
        return nums[mid]

    def getClosest(self, val1, val2, target):
        if target - val1 >= val2 - target:
            return val2
        else:
            return val1

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findClosest([2, 3, 5, 7, 8, 11], 9)
    print(ans)
