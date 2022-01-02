#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)] # record value and index
        res = [0] * n

        def merge_sort(arr, left, right):
            # merge_sort [left, right] for small to large, in place
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        def merge(arr, left, right, mid):
            # merge [left, mid] and [mid, right]
            i = left
            j = mid
            # use temp to temporatrily store sorted array
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i
                    res[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            #when one of the subarrays is empty
            while i < mid:
                #j - mid number jump to the left side of arr[i]
                res[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1

            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]
        merge_sort(arr, 0, n)
        return res


# @lc code=end
