import os
import collections

class Solution:
    def process_file(file_name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)

        data = list(csv.reader(open(file_path)))

    def is_undirected_graph_circled(self, adj_matrix):
        n = len(adj_matrix)
        degrees = [0] * n
        q = collections.deque()
        visited = []
        for i in range(0, n):
            degrees[i] = sum([int(value) for value in adj_matrix[i]])
            if degrees[i] <= 1:
                q.append(i)
                visited.append(i)

        while q:
            i = q.get()
            for j in range(0, n):
                if int(adj_matrix[i][j]) == 1:
                    degrees[j] -= 1
                    if degrees[j] == 1:
                        q.append(j)
                        visited.append(j)
        if len(visited) == n:
            return False
        else:
            return True
