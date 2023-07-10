class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # approach: union find, decrement result every time a union succeeds
        
        par = [i for i in range(n)]
        rank = [1] * n
        res = n
        
        def find(n):
            p = par[n]
            
            while p != par[p]:
                # path compression
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(p1, p2):
            nonlocal res
            p1, p2 = find(p1), find(p2)
            
            if p1 == p2:
                return
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            res -= 1
        
        for p1, p2 in edges:
            union(p1, p2)
        '''        
        # make sure all nodes point to roots
        for i in range(n):
            p = par[i]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
                par[i] = p

        hashset = set()
        for i in range(n):
            hashset.add(par[i])'''
        
        return res