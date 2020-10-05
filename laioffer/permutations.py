class Solution:
    def permutation(self, set):
        result = []
        if set is None:
            return result
        array = list(set)
        self.dfs(array, 0, result)
        return result
    def dfs(self, array, index, result):
        if index == len(array):
            result.append(array.copy())
            return

        for i in range(index, len(array)):
            self.swap(array, index, i)
            self.dfs(array, index + 1, result)
            self.swap(array, index, i)
    def swap(self, array, left, right):
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp

if __name__ == "__main__":
    solution = Solution()
    result = solution.permutation("123")
    print(result)
