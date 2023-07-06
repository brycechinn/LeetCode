class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # approach: number of islands, except keep track of max island size
        
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1
            
            while q:
                r, c = q.popleft()
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                
                for x, y in directions:
                    # new row and col
                    nr, nc = r + x, c + y
                    
                    if (nr in range(m) and 
                        nc in range(n) and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        
        return res