class Solution:
    def find_duplicate(self, array):
        dic = {}
        res = []
        for x in array:
            dic[x] = dic.get(x, 0) + 1
            if dic[x] > 1 and x not in res:
                res.append(x)
        return res



# Main class function Test
if __name__ == '__main__':
    input = [2, 2, 8, 4, 5, 6, 4, 8, 8, 7]
    solution = Solution()
    ans = solution.find_duplicate(input)
    print(ans)
