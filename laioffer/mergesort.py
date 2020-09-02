class Solution:
    def mergeSort(self, array):
        if len(array) == 0:
            return

        helper = [0]*len(array)
        self.mergesort_helper(array, helper, 0, len(array)- 1)


    def mergesort_helper(self, array, helper, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.mergesort_helper(array, helper, left, mid)
        self.mergesort_helper(array, helper, mid +1 , right)

        self.merge(array, helper, left, mid, right)



    def merge(self, array, helper, left, mid, right):
        for i in range(left, right + 1):
            helper[i] = array[i]
        leftIndex = left
        rightIndex = mid+ 1
        while leftIndex <= mid and rightIndex <= right:
            if helper[leftIndex] <= helper[rightIndex]:
                array[left] = helper[leftIndex]
                left += 1
                leftIndex += 1
            else:
                array[left] = helper[rightIndex]
                left += 1
                rightIndex += 1
        while leftIndex <= mid:
            array[left] = helper[leftIndex]
            left += 1
            leftIndex += 1

# Main class function Test
if __name__ == '__main__':
    input = [2, 8, 4, 5, 6, 7]
    solution = Solution()
    solution.mergeSort(input)
    print(input)
