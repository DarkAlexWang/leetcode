import collections
class Solution:
    def same_freq_as_num(self, arr):
        dic = collections.defaultdict()
        for num in arr:
            dic[num] = dic.get(num, 0) + 1
        res = []
        for key, value in dic.items():
            if key == value:
                res.append(value)
        return max(res) if res else -1

if __name__ == '__main__':
    solution = Solution()
    ans = solution.same_freq_as_num([3, 1, 4, 5, 3, 2, 1, 3])
    print(ans)
