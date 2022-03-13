class Solution:
    def find_max_diff_index(self, arr):
        dic = {}
        res = 0
        for i, num in enumerate(arr):
            if num in dic:
                res = max(res, i - dic[num])
            else:
                dic[num] = i
        return res

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.find_max_diff_index([1, 2, 2, 2, 1])
    print(ans1)
    ans2 = solution.find_max_diff_index([1, 2, 3, 4, 5, 2, 2, 2])
    print(ans2)
