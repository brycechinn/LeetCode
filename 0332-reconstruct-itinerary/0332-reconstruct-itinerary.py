class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # approach: sort tickets, adjacency list of src : list of dst, 
        # then backtracking DFS to find a valid path
        
        tickets.sort()
        adj = collections.defaultdict(list)
        res = ['JFK']
        
        for src, dst in tickets:
            adj[src].append(dst)
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if not adj[src]:
                return False
            
            temp = adj[src].copy()
            for i, nei in enumerate(temp):
                # consider neighbor
                adj[src].pop(i)
                res.append(nei)
                
                if dfs(nei):
                    return True
                
                # invalid path, backtrack
                adj[src].insert(i, nei)
                res.pop()
            
            return False
                
        dfs('JFK')
        return res