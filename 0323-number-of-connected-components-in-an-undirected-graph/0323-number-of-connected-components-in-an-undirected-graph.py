class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # approach 1: DFS
        '''
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
            if i in visited:
                continue
                
            dfs(i)
            res += 1
                
        return res
        '''
    
        # approach 2: union find
        
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n):
            p = par[n]
            
            while p != par[p]:
                p = par[p]
            
            return p
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        res = n
        for n1, n2 in edges:
            if not union(n1, n2):
                continue
            
            res -= 1
        
        return res