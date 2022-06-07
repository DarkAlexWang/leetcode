class Solution:
    def quickSort(self, arr):
        low, high = 0, len(arr) - 1
        self.quickSort_helper(arr, low, high)

    def quickSort_helper(self, arr, low, high):
        if low > high:
            return
        pi = self.partition(arr, low, high)
        self.quickSort_helper(arr, low, pi - 1)
        self.quickSort_helper(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i, j = low, high- 1
        while i <= j:
            if arr[i] < pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        arr[i], arr[high]  = arr[high], arr[i]
        return i

if __name__ == '__main__':
    solution = Solution()
    #input = [1, 4, 3, 9, 7, 8]
    input = [0, 1, 2, 6, 5]
    solution.quickSort(input)
    print(input)
