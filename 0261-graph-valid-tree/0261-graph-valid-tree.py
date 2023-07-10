class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # approach 1: union find, return False if union cannot be done 
        # or num components > 1
        '''
        par = [i for i in range(n)]
        rank = [1] * n
        components = n
        
        def find(n):
            p = par[n]
            
            while p != par[p]:
                # path compression
                par[p] = par[par[p]]
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
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            
            components -= 1
            
        return components == 1
        '''
        # approach 2: adjacency list -> DFS, return False if cycle or 
        # visited nodes < n
        
        adj = collections.defaultdict(list)
        visited = set()
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            
            for neighbor in adj[i]:
                if neighbor == prev:
                    continue
                    
                if not dfs(neighbor, i):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n