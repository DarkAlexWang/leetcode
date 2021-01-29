# @lc lang=python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_k = len(nums) - k
        low, high = 0, len(nums) - 1
        while low <= high:
            res = self.partition(nums, low, high)
            if res == new_k:
                return nums[res]
            elif res > new_k:
                high = res - 1
            else:
                low =res + 1

    def partition(self, nums, low, high):
        if low >= high:
            return low
        pivot = nums[high]
        i, j = low, high - 1
        while i <= j:
            if nums[i] < pivot:
                i += 1
            elif nums[j] > pivot:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
