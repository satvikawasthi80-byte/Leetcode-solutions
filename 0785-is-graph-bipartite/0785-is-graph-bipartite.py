class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] != -1:
                continue

            queue = [start]
            color[start] = 0

            for node in queue:
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

                    elif color[neighbor] == color[node]:
                        return False

        return True