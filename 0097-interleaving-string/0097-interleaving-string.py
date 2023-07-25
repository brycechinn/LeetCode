class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            if i1 == len(s1) and i2 == len(s2):
                return True
            
            c1 = s1[i1] if i1 < len(s1) else ''
            c2 = s2[i2] if i2 < len(s2) else ''
            c3 = s3[i1 + i2]
            
            if c1 != c3 and c2 != c3:
                return False
            
            if c1 == c3 and c2 == c3:
                dp[(i1, i2)] = dfs(i1 + 1, i2) or dfs(i1, i2 + 1)
            elif c1 == c3:
                dp[(i1, i2)] = dfs(i1 + 1, i2)
            else:
                dp[(i1, i2)] = dfs(i1, i2 + 1)
            
            return dp[(i1, i2)]
        
        return dfs(0, 0)