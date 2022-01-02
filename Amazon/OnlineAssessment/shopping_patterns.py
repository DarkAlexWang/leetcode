import collections
import sys
class ShoppingPatterns:
    def minTrioDegree(self, n, edges):
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        degree = {n: len(graph[n]) for n in graph}

        res = sys.maxsize
        for n in graph:
            for m in graph[n]:
                for o in graph[n] & graph[m]:
                    res = min(res, degree[n] + degree[m] + degree[o] - 6)
                    graph[o].discard(n)
                graph[m].discard(n)
        return res if res < sys.maxsize else -1

if __name__ == "__main__":
    solution = ShoppingPatterns()
    ans1 = solution.minTrioDegree(6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]])
    print(ans1)
    ans2 = solution.minTrioDegree(7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]])
    print(ans2)
