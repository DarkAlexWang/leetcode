class Solution:
    def permutation(self, string):
        res = []
        if string is None:
            return res
        array = list(string)
        self.helper(array, 0, res)
        return res
    def helper(self, array, index, res):
        if index == len(array):
            res.append(array)
            return
        used = set()
        i = index
        while i < len(array):
            if used.add(array[i]):
                self.swap(array, i, index)
                self.helper(array, index + 1, res)
                self.swap(array, i, index)

    def swap(self, array, left, right):
        tmp = array[left]
        array[left] = array[right]
        array[right] = tmp
