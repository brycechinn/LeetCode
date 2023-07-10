class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # approach: union find, then count unique parents
        
        par = [i for i in range(n)]
        rank = [1] * n
        
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
                print('redundant connection detected')
        
        # compress par
        for i in range(n):
            p = par[i]

            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
                par[i] = p

        hashset = set()
        for i in range(n):
            hashset.add(par[i])
        
        return len(hashset)