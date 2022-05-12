class Solution:
    def strstr(self, large, small):
        if len(large) < len(small):
            return -1
        if len(small) == 0:
            return 0
        for i in range(len(large) - len(small)):
            if large[i: (i +len(small))] == small:
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    res = solution.strstr('abcdeg', 'blc')
    print(res)
