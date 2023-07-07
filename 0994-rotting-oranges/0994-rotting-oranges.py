class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # approach: multi-source BFS
        
        m, n = len(grid), len(grid[0])
        visited = set()
        total, found = 0, 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    total += 1
                
                if grid[r][c] == 2:
                    visited.add((r, c))
        
        def bfs():
            nonlocal found
            q = collections.deque()
            time = 0
            
            for v in visited:
                q.append(v)
                
            while q:
                size = len(q)
                
                for _ in range(size):
                    r, c = q.popleft()
                    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                    
                    for dr, dc in directions:
                        # new row, new col
                        nr, nc = r + dr, c + dc

                        if (nr not in range(m) or 
                            nc not in range(n) or 
                            grid[nr][nc] != 1 or 
                            (nr, nc) in visited):
                            continue

                        visited.add((nr, nc))
                        q.append((nr, nc))
                        found += 1
                
                time += 1

            return max(time - 1, 0)
        
        time = bfs()
        return time if total == found else -1