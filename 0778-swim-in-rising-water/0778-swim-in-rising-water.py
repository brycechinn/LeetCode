class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # approach: modified Djikstras to find path with min highest 
        # elevation point
        
        n = len(grid)
        visited = set()
        
        heap = []
        heap.append((grid[0][0], 0, 0))
        visited.add((0, 0))
        
        while heap:
            highest, r, c = heapq.heappop(heap)
            
            # potential new res
            if r == n - 1 and c == n - 1:
                return highest

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in directions:
                # new row and col
                nr, nc = r + dr, c + dc
                
                if (nr not in range(n) or 
                    nc not in range(n) or 
                    (nr, nc) in visited):
                    continue
                
                heapq.heappush(heap, (max(highest, grid[nr][nc]), nr, nc))
                visited.add((nr, nc))