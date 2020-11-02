class Solution:
    def quickSort(self, arr):

        low, high = 0, len(arr)
        self.quicksort_helper(arr, low, high)

    def quicksort_helper(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quicksort_helper(arr, low, pi - 1)
            self.quicksort_helper(arr, pi + 1, high)

    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

if __name__ == '__main__':
    input = [2, 8, 4, 5, 7, 1]
    solution = Solution()
    solution.quickSort(input)
    print(input)
