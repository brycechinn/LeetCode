class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # approach: adjacency list -> DFS
        
        prereqs = collections.defaultdict(list)
        visited = set()

        for a, b in prerequisites:
            prereqs[a].append(b)
            
        def dfs(c):
            if c in visited:
                return False
            
            if not prereqs[c]:
                return True
            
            visited.add(c)
            
            for p in prereqs[c]:
                if not dfs(p):
                    return False
            
            visited.remove(c)
            
            # remove prereqs from course to prevent repeating work
            prereqs[c] = []
            return True

        for c in range(numCourses):         
            if not dfs(c):
                return False

        return True