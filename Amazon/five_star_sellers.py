import heapq
class FiveStarSellers(object):
    def solution(self, n, arr, threshold):
        def increase(rate, total):
            return (rate+1) / (total+1) - rate / total
        current = 0
        hq = []
        for rate, total in arr:
            current += rate / total
            heapq.heappush(hq, (-increase(rate, total), rate , total))
        res = 0
        while current/n < threshold / 100.0:
            res+=1
            inc , rate, total = heapq.heappop(hq)
            current = current - inc
            rate, total = rate+1, total+1
            heapq.heappush(hq,(-increase(rate, total), rate , total))
        return res

if __name__ == "__main__":
    solution = FiveStarSellers()
    res = solution.solution(3, [[4,4], [1,2], [3, 6]], 77)
    print(res)
