class Solution:
    def first_occurrence(self, array, target):

        if len(array) == 0 or not array:
            return -1
        left = 0
        right = len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid]  >= target:
                right = mid
            else:
                left = mid

        if array[left] == target:
            return left
        elif array[right] == target:
            return right
        return -1

    def last_occurrence(self, array, target):

        if len(array) == 0 or not array:
            return -1
        left = 0
        right = len(array) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid]  <= target:
                left = mid
            else:
                right = mid

        if array[left] == target:
            return left
        elif array[right] == target:
            return right
        return -1
