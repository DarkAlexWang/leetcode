class Solution:
    def removeduplicateI(self, string):
        if string == '':
            return string
        end = 0
        array = list(string)
        for i in range(1, len(array)):
            if end == -1 or array[i] != array[end]:
                array[end] = array[i]
                end += 1
            else:
                end -= 1
                while i + 1 < len(array) and array[i] == array[i -1]:
                    i += 1
        res = ''
        for i in range(end + 1):
            res += array[i]
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.removeduplicateI('aabbcc')
    print(res)
