class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # approach: add coastal nodes to pacific and atlantic, then dfs from
        # each coastal node and return nodes that belong to both sets
        
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, lowest, is_pacific):
            if (r not in range(m) or 
                c not in range(n) or 
                heights[r][c] < lowest or 
                (is_pacific and (r, c) in pacific) or
                (not is_pacific and (r, c) in atlantic)):
                return

            if is_pacific:
                pacific.add((r, c))
            
            else:
                atlantic.add((r, c))

            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], is_pacific)
        
        for r in range(m):
            dfs(r, 0, heights[r][0], True)
            dfs(r, n - 1, heights[r][n - 1], False)
            
        for c in range(n):
            dfs(0, c, heights[0][c], True)
            dfs(m - 1, c, heights[m - 1][c], False)

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res