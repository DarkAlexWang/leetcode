import heapq
class Solution:
    def bestCombos(self, nums, k):
        heap = []
        heapq.heapify(heap)
        nums.sort()
        self.dfs(nums, 0, 0, heap, k)
        res = []
        top = [0 for _ in range(k)]
        for i in range(k -1, -1, -1):
            top = heapq.heappop(heap)
            res.append(top)
        return res

    def dfs(self, nums, start, curSum, heap, k):
        heapq.heapify(heap)
        if len(heap) == k:
            if heap[0] < curSum:
                heapq.heappop(heap)
                heapq.heappush(heap, curSum)

        else:
            heapq.heappush(heap, curSum)


        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i -1]:
                # skip duplicate
                continue
            curSum += nums[i]
            self.dfs(nums, i + 1, curSum, heap, k)
            curSum -= nums[i]

if __name__ == "__main__":
    solution = Solution()
    res1 = solution.bestCombos([3, 5, -2], 3)
    print(f'res1:{res1}')
    res2 = solution.bestCombos([1, 2, 3, 1000], 4)
    print(f'res2:{res2}')
    res3 = solution.bestCombos([0, 0, 0, 0, 0], 3)
    print(f'res3:{res3}')
