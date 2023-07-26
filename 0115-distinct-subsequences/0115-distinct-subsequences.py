class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # approach 1: top-down DP with memoization
        
        if len(s) < len(t):
            return 0
        
        dp = {}
        
        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j) + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            
            return dp[(i, j)]
        
        return dfs(0, 0)