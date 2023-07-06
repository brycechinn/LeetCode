class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # approach: DFS from each coastal node and return nodes that belong
        # to both pacific and atlantic sets
        
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, lowest, visited):
            if (r not in range(m) or 
                c not in range(n) or 
                heights[r][c] < lowest or 
                (r, c) in visited):
                return

            visited.add((r, c))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visited)
        
        for r in range(m):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, n - 1, heights[r][n - 1], atlantic)
            
        for c in range(n):
            dfs(0, c, heights[0][c], pacific)
            dfs(m - 1, c, heights[m - 1][c], atlantic)

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res