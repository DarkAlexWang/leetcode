#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def quickSort(self, nums, l, r):
        if l >= r:
            return
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos - 1)
        self.quickSort(nums, pos + 1, r)

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)


#    def bubblesort(self, nums):
#        for i in range(len(nums), 0, -1):
#            for j in range(i - 1):
#                if not self.compare(nums[j], nums[j + 1]):
#                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
#        return str(int("".join(map(str, nums))))
#
#    def larestNumber(self, nums):
#        nums = self.mergeSort(nums, 0, len(nums) - 1)
#        return str(int("".join(map(str, nums))))
#
#    def mergeSort(self, nums, l, r):
#        if l > r:
#            return
#        if l == r:
#            return [nums[l]]
#        mid = (l + r) // 2
#        left = self.mergeSort(nums, l, mid)
#        right = sefl.mergeSort(nums, mid + 1, r)
#        return self.merge(left, right)
#
#    def merge(self, l1, l2):
#        res, i, j = [], 0, 0
#        while i < len(l1) and j < len(l2):
#            if not self.compare(l1[i], l2[j]):
#                res.append(l2[j])
#                j += 1
#            else:
#                res.append(l1[i])
#                i += 1
#        res.extend(l1[i:] or l2[j:])
#        return res
# @lc code=end
