class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # approach: BFS
        
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            
            while q:
                r, c = q.popleft()
                
                # right, left, up, down
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                
                for x, y in directions:
                    # new row and col
                    nr, nc = r + x, c + y
                    
                    if (nr in range(m) and 
                        nc in range(n) and 
                        grid[nr][nc] == '1' and 
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands