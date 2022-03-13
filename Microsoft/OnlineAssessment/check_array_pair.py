class Solution:
    def check_array_pair(self, arr):
        dic = dict()
        for ele in arr:
            if ele in dic:
                del dic[ele]
            else:
                dic[ele] = 1
        return dic == {}

if __name__ == "__main__":
    solution = Solution()
    print(solution.check_array_pair([1, 2, 2, 1]))
    print(solution.check_array_pair([1, 3, 2, 2, 1]))
