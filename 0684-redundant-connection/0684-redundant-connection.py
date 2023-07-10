class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # approach: union find
        
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = par[n]
            
            while p != par[p]:
                # path compression
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(p1, p2):
            p1, p2 = find(p1), find(p2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for p1, p2 in edges:
            if not union(p1, p2):
                return [p1, p2]