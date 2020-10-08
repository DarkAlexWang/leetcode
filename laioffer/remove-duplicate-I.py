class Solution:
    def removeduplicateI(self, string):
        if string == '':
            return string
        end = 0
        array = list(string)
        for i in range(len(array)):
            if i == 0 or array[i] != array[end - 1]:
                array[end] = array[i]
                end += 1
        res = ''
        for i in range(end):
            res += array[i]
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.removeduplicateI('aabbcc')
    print(res)
