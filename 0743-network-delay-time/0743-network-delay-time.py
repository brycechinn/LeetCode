class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # approach: Djikstra's Shortest Path from node k
        
        # 1. build adjacency list
        adj = collections.defaultdict(list)
        
        for u, v, w in times:
            adj[u].append((w, v))
        
        # 2. Djikstra's via BFS with min heap of (dist from source, node)
        dists = [float('inf')] * (n + 1)
        visited = set()

        def bfs(src):
            heap = []
            heap.append((0, src))

            while heap:
                path, i = heapq.heappop(heap)
                
                if i in visited:
                    continue
                
                visited.add(i)
                dists[i] = min(dists[i], path)
                
                for dist, nei in adj[i]:
                    if nei not in visited:
                        heapq.heappush(heap, (path + dist, nei))
                
        bfs(k)
        return max(dists[1:]) if len(visited) == n else -1