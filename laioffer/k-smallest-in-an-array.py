import heapq
class Solution:
    def ksmallest(self, nums, k):
        heap = []
        res = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(k):
            res.append(heapq.heappop(heap))
        return res

if __name__ == '__main__':
    solution = Solution()
    arry = [2, 4, 5, 3, 6]
    k = 2
    res = solution.ksmallest(arry, k)
    print(res)
