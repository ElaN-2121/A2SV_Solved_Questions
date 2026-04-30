class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        white = 1
        black = 2
        n= len(graph)
        colors = [0] * n

        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color
            colors[node] = color
            next_color = 2 if color == 1 else 1
            for nei in graph[node]:
                if not dfs(nei, next_color):
                    return False
            return True
            
        for i in range(n):
            if colors[i] == 0:
                if not dfs(i, white):
                    return False
        return True

