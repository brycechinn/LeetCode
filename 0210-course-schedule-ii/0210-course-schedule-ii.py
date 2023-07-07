class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # approach: adjacency list -> topological sort
        
        prereqs = collections.defaultdict(list)
        visited, cycle = set(), set()
        has_cycle = False
        res = []
        
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        def dfs(c):
            nonlocal has_cycle
            
            if c in cycle:
                has_cycle = True
                return
            
            if c in visited:
                return

            cycle.add(c)
            
            for p in prereqs[c]:
                dfs(p)
                
            cycle.remove(c)
            visited.add(c)
            res.append(c)
        
        for c in range(numCourses):
            dfs(c)
        
        return res if not has_cycle else []