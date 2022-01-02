class OptimizeBox:
    def optimize(self, arr):
        array_sum = 0
        for num in arr:
            array_sum += num
        arr.sort()
        max_num, idx = 0, 0
        while idx < len(arr) and max_num * 2 < array_sum:
            max_num += arr[idx]
            idx += 1

        # idx now is the first element in box A
        idx -= 1

        res = [None for _ in range(len(arr) - idx)]
        for i in range(len(arr) - idx):
            res[i] = arr[idx + i]
        return res



if __name__ == "__main__":
    solution = OptimizeBox()
    ans1 = solution.optimize([4, 5, 2, 3, 1, 2])
    print(f"ans1: {ans1}")
    ans2 = solution.optimize([1, 2, 3, 5, 8])
    print(f"ans2: {ans2}")
