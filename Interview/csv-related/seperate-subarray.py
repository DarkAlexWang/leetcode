# Given an array of integers greater than zero, find if it is possible to split
# it in two subarrays (without reordering the elements),
# such that the sum of the two subarrays is the same.
# Print the two subarrays.

class Solution:
    def isItPossibleToSplitInTwoArrays(self, arr):
        left_sum = 0
        right_sum = sum(arr)
        for i, n in enumerate(arr):
            if left_sum == right_sum:
                print("left array: " + str(arr[:i]))
                print("right array: " + str(arr[i:]))
                return True
            right_sum -= n
            left_sum += n
        return False

    def isItPossibleToSplitInTwoArrays2(self, arr):
        if not arr or len(arr) == 1:
            return False
        i, j = -1, len(arr)

        left_sum = 0
        right_sum = 0
        while j - i > 1:
            if left_sum < right_sum:
                i += 1
                left_sum += arr[i]
            elif left_sum > right_sum:
                j -= 1
                right_sum += arr[j]
            elif j - i > 2:
                i += 1
                j -= 1
                left_sum += arr[i]
                right_sum -= arr[j]
            else:
                i += 1
                left_sum += arr[i]
        if left_sum == right_sum:
            print("left array: " + str(arr[:i]))
            print("right array: " + str(arr[i:]))
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    input = [1, 4, 5, 5, 3, 9]
    output = solution.isItPossibleToSplitInTwoArrays(input)
    output2 = solution.isItPossibleToSplitInTwoArrays2(input)
    print(output)
    print(output2)
