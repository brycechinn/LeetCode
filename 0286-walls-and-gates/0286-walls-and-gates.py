class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # approach: multi-source BFS starting at gates
        
        INF = pow(2, 31) - 1
        m, n = len(rooms), len(rooms[0])
        
        q = collections.deque()
        
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    # (row, column, distance)
                    q.append((r, c, 0))
        
        while q:
            r, c, d = q.popleft()
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                # new row and col
                nr, nc = r + dr, c + dc
                
                if (nr not in range(m) or 
                    nc not in range(n) or 
                    rooms[nr][nc] != INF):
                    continue
                
                rooms[nr][nc] = d + 1
                q.append((nr, nc, d + 1))
                    