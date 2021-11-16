import sys
class OptimalUtilization:
    def get_pairs(self, a, b, target):
        sorted(a, key = lambda x: x[1])
        sorted(b, key = lambda x: x[1])
        #a.sort()
        #b.sort()
        res = []
        max_value = -sys.maxsize
        m, n = len(a), len(b)
        i, j = 0, n - 1
        while i < m and j >= 0:
            sum_value = a[i][1] + b[j][1]
            if sum_value > target:
                j -= 1
            else:
                if max_value <= sum_value:
                    if max_value < sum_value:
                        max_value = sum_value
                        res.clear()

                    res.append([a[i][0], b[j][0]])
                    index = j - 1
                    while index >= 0 and b[index][1] == b[index + 1][1]:
                        index -= 1
                        res.append([a[i][0], b[index][0]])
                i += 1
        return res

if __name__ == "__main__":
    solution = OptimalUtilization()
    ans1 = solution.get_pairs([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7)
    print(ans1)
    ans2 = solution.get_pairs([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10)
    print(ans2)
