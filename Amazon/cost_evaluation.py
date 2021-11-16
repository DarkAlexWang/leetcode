import math

class UnionFindClass:
    def UnionFind(n):
        parent = []
        rank = []
        size  = n
        for i in range(n):
            parent[i] = i
            rank[i] = 1
    def find(x):
        root = x
        if parent[x] != x:
            root = find(parent[x])

        return root

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA == rootB:
            return
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
            rank[rootA] += rank[rootB]

        else:
            parent[rootA] = rootB
            rank[rootB] += root[rootA]
class Solution:
    def cost_evaluation(self, n, arr):
        uf_class = UnionFindClass()
        uf = uf_class.UnionFind()
        for i in range(len(arr)):
            uf_class.union(arr[i][0], arr[i][1])
        res = 0
        for i in range(n):
            if uf_class.parent[i] == i:
                res += math.ceil(math.sqrt(uf_class.rank[i]))
        return res
        #if n < 2:
        #    return n
        #graph = {}

        #for i in range(n):
        #    graph.append(i, [])

        #for num in arr:
        #    x = num[0]
        #    y = num[1]
        #    graph[x].append(y)
        #    graph[x].append(y)

        #island = 0
        #res = 0
        #visited = []
        #for :
        #    if

if __name__ == "__main__":
    solution = Solution()
    res1 = solution.cost_evaluation(10, [[2, 6], [3, 5], [0, 1], [2, 9], [5, 6]])
    print(res1)
    res2 = solution.cost_evaluation(4, [[0, 2], [1, 2]])
    print(res2)
