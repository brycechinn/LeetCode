class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # approach 1: top-down DP, memoization of (i, j) : min operations
        
        dp = {}
        
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(dfs(i, j + 1),     # insert
                                     dfs(i + 1, j),     # delete
                                     dfs(i + 1, j + 1)) # replace
            return dp[(i, j)]

        return dfs(0, 0)           