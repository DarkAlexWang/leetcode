import heapq
class process:
    def process(self, arr, exe):
        self.arrTime = arr
        self.exeTime = exe
class Solution:
    def shortest_job_first(self, req, dur):
        if req == None or dur == None or len(req) != len(dur):
            return 0
        index, length = 0, len(req)
        waitTime, curTime = 0, 0
        pq = []
        if p1.exeTime == p2.exeTime:
            return p1.arrTime - p2.arrTime
        return p1.exeTime - p2.exeTime

        while pq or index < length:
            if pq:
                cur = pq.heappushpop()
                waitTime += curTIme - cur.arrTime
                curTime += cur.exeTime
                while index < length and curTime >= req[index]:
                    pq.heappush((req[index], dur[index+1]))
            else:
                pq.heappush(req[index], dur[index])
                curTime = req[index + 1]

        return round(waitTime/length, 2)

if __name__ == '__main__':
    solution = Solution()
    res = solution.shortest_job_first([1,2, 3, 4], [1, 2, 3, 4])
    print(res)
