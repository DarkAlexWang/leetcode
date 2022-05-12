import collections
class Solution:
    def common_number(self, a, b):
        res = []
        count_a = collections.defaultdict()
        count_b = collections.defaultdict()
        for num in a:
            count_a[num] = count_a.get(num, 0) + 1
        for num in b:
            count_b[num] = count_b.get(num, 0) + 1
        for key, value in count_a.items():
            if key in count_b:
                appear = min(value, count_b[key])
                for i in range(appear):
                    res.append(key)
        return res

if __name__ == "__main__":
    solution = Solution()
    ans = solution.common_number([1, 2, 2, 5, 7, 8, 9], [1, 2, 2, 4, 6, 7, 8, 10])
    print(ans)
