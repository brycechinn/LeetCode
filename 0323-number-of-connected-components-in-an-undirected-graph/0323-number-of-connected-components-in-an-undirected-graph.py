class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # approach: dfs
        
        adj = {}
        
        for node, nei in edges:
            if node not in adj:
                adj[node] = []
            
            if nei not in adj:
                adj[nei] = []
            
            adj[node].append(nei)
            adj[nei].append(node)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            if node not in adj:
                return
            
            for nei in adj[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
                
        return res