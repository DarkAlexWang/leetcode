import collections
class Turnstile:
    def get_times(self, time, direction):
        enters = collections.deque()
        exits = collections.deque()
        n = len(time)
        for i in range(n):
            q = exits if direction[i] == 1 else enters
            q.append(i)

        res = [None for _ in range(n)]
        lastTime = -2
        lastQ = exits
        while len(enters) > 0 and len(exits) > 0:
            currentTime = lastTime + 1
            peekEnterTime = time[enters[-1]]
            peekExitTime = time[exits[-1]]
            if currentTime < peekEnterTime and currentTime < peekExitTime:
                # The turnstile was not used
                # Take whoever has the earlist time or if enter == exit, take
                # exit
                q = enters if peekEnterTime < peekExitTime else exits
                personIdx = q.popleft()
                res[personIdx] = time[personIdx]
                lastTime = time[personIdx] # time
                lastQ = q
            else:
                # Turnstile was used last second
                if currentTime >= peekEnterTime and currentTime >= peekExitTime:
                    # Have people waiting at both ends
                    # Prioitize last direction
                    q = lastQ
                else:
                    # current >= enters.peek() or current >= exits.peek()
                    q = enters if currentTime >= peekEnterTime else exits # take whatever that's queueing

                personIdx = q.popleft()
                res[personIdx] = currentTime
                lastTime = currentTime
                lastQ = q
        q = enters if len(enters) > 0 else exits
        while len(q) > 0:
            currentTime = lastTime + 1
            personIdx = q.popleft()
            if currentTime < time[personIdx]:
                # The turnstile was not used
                currentTime = time[personIdx]
            res[personIdx] = currentTime
            lastTime = currentTime
        return res



if __name__ == "__main__":
    solution = Turnstile()
    ans = solution.get_times([0, 0, 1, 5], [0, 1, 1, 0])
    print(ans)
