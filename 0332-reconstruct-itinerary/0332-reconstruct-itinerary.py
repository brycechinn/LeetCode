class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # approach: sort tickets, adj list of src : list of dst,
        # backtracking DFS to find valid path
        
        tickets.sort()
        adj = {}
        
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            
            adj[src].append(dst)

        res = ['JFK']
        
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            
            if node not in adj:
                return False
            
            for i, nei in enumerate(adj[node].copy()):
                adj[node].pop(i)
                res.append(nei)
                
                if dfs(nei):
                    return True
                
                # if invalid path, backtrack
                adj[node].insert(i, nei)
                res.pop()
            
            return False
        
        dfs('JFK')
        return res