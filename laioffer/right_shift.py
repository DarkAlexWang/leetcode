class Solution:
    def right_shift(self, string, n):
        if len(string) <= 1:
            return string
        array = list(string)
        n %= len(array)
        self.reverse(array, len(array) - n, len(array) - 1)
        self.reverse(array, 0, len(array) - n - 1)
        self.reverse(array, 0, len(array) - 1)
        return "".join(array)
    def reverse(self, array, left, right):
        while left < right:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()
    ans = solution.right_shift("abcdef", 2)
    print(ans)
