import collections
class CountSwap:
    def cost(self, arr):
        dic = collections.defaultdict()
        sortedArr = [None for _ in range(len(arr))]
        for i in range(len(arr)):
            dic[arr[i]] = i
            sortedArr[i] = arr[i]

        sortedArr.sort()

        res = 0
        for i in range(len(sortedArr)):
            targetVal = sortedArr[i]
            targetIndex = dic[targetVal]
            if i != targetIndex:
                res += 1
                valToSwap = arr[i]
                dic[valToSwap] = targetIndex
                temp = arr[i]
                arr[i] = arr[targetIndex]
                arr[targetIndex] = temp
        return res

if __name__ == "__main__":
    solution = CountSwap()
    ans1 = solution.cost([5, 4, 1, 2])
    ans2 = solution.cost([1, 20, 6, 4, 5])
    print(ans1)
    print(ans2)
