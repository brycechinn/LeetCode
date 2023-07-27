class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # approach: top-down DP, memoization of (i, j) : is match

        dp = {}
        
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False

            if (i, j) in dp:
                return dp[(i, j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                dp[(i, j)] = (match and dfs(i + 1, j) or # use *
                              dfs(i, j + 2))             # don't use *
                return dp[(i, j)]
            
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)