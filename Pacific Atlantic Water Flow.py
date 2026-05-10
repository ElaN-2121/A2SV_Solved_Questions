class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited = set()
        atlantic_visited = set()
        rows, cols = len(heights), len(heights[0])
        def isValid(nr, nc, r,c):
            if (0 <= nr <rows and 0 <= nc < cols) and heights[nr][nc] >= heights[r][c]:
                return True
            return False

        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc, r, c) and (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific_visited)        # top row
            dfs(rows-1, c, atlantic_visited)  # bottom row

        for r in range(rows):
            dfs(r, 0, pacific_visited)        # left column
            dfs(r, cols-1, atlantic_visited)  
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])
        return result


