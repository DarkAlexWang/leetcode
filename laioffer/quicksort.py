class Solution:
    def quickSort(self, array):
        if len(array) == 0:
            return

        self.quicksort_helper(array, 0, len(array) - 1)
        return array

    def quicksort_helper(self, array, left, right):
        if left >= right:
            return
        pivotPos = self.partition(array, left, right)
        self.quicksort_helper(array, left, pivotPos)
        self.quicksort_helper(array, pivotPos + 1, right)

    def partition(self, array, left, right):
        pivotIndex = self.pivotIndex(array, left, right)
        pivot = array[pivotIndex]
        self.swap(array, pivotIndex, right)
        leftBound = left
        rightBound = right -1
        while leftBound <= rightBound:
            if array[leftBound] < pivot:
                leftBound += 1
            elif array[rightBound] >= pivot:
                rightBound -= 1
            else:
                self.swap(array, leftBound, rightBound)
                leftBound += 1
                rightBound -= 1
        self.swap(array, leftBound, right)
        return leftBound

    def pivotIndex(self, array, left, right):
        return right - 1

    def swap(self, array, left, right):
        temp = array[left]
        array[left] = array[right]
        array[right] = temp

# Main class function Test
if __name__ == '__main__':
    input = [2, 8, 4, 5, 6, 7]
    solution = Solution()
    solution.quickSort(input)
    print(input)
