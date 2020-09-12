class Solution:
    def unknownsizebinarysearch(self, dic, target):
        if not dic:
            return -1
        left = 0
        right = 1

        while dic.get(right) != null and dic.get(rigth) < target:
            left = right
            right *= 2

        return self.binarysearch(dic, target, left, right)

    def binarysearch(self, dic, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if dic.get(mid) == null or dic.get(mid) > target:
                right = mid - 1
            elif dic.get(mid) < target:
                left = mid + 1
            else:
                return mid
        return -1
