class Solution:
    def recentitems(self, logs):
        stack = []
        res = []
        stack = set()
        for item in logs[::-1]:
            stack.add(item)
        for item in stack:
            res.append(item)
        return res


if __name__ == "__main__":
    solution = Solution()
    res1 = solution.recentitems(['Echo Show 8', 'Kindle Oasis', 'Fire TV Stice', 'Echo Show 8'])
    print(res1)
    res2 = solution.recentitems(['Smartphone', 'Television', 'Smartphone', 'Television'])
    print(res2)
    res3 = solution.recentitems(['Book1', 'Book2', 'Book3', 'Book1', 'Book3'])
    print(res3)
