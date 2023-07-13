class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # approach: adjacency list of p1 : (dist, p2), then Prim's Algorithm
        # -> MST via BFS
        
        # 1. adjacency list of p1 : (dist, p2)
        N = len(points)
        adj = collections.defaultdict(list)
        res = 0
        
        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        # 2. Prim's Algorithm -> MST via BFS
        def bfs():
            nonlocal res
            
            visited = set()
            heap = [(0, 0)]
            
            while len(visited) < N:
                dist, i = heapq.heappop(heap)
                
                if i in visited:
                    continue
                
                visited.add(i)
                res += dist
                
                for nei in adj[i]:
                    nei_dist, nei_i = nei
                    
                    if nei_i not in visited:
                        heapq.heappush(heap, nei)
        
        bfs()
        return res          