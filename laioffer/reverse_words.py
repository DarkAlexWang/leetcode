class Solution:
    def reverse_words(self, words):
        array = list(words)
        self.reverse(array, 0, len(array) - 1)
        start = 0
        for i in range(len(array)):
            if array[i] != ' ' and (i == 0 or array[i - 1] == " "):
                start = i
            if array[i] != ' ' and (i == len(array) - 1 or array[i + 1] == ' '):
                self.reverse(array, start, i)
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
    ans = solution.reverse_words("This is the words to be reversed")
    print(ans)
