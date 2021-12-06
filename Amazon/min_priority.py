import collections
class Solution:
    def minPriority(self, arr):
        n = len(arr)
        dic = collections.defaultdict()
        for val in arr:
            dic[val] = dic.get(val, 0) + 1

        dic = dict(sorted(dic.items()))
        print(dic)
        mp = {}
        priority = 1
        for val in dic.keys():
            mp[val] = priority
            priority += 1
        for i in range(n):
            arr[i] = mp[arr[i]]
        return arr

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.minPriority([1, 4, 8, 4])
    ans2 = solution.minPriority([2, 9, 3, 2, 3])
    print(ans1)
    print(ans2)
