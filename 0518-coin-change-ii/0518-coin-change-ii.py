class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # approach 1: backtracking DFS (TLE)
        '''
        res = 0
        
        def dfs(i, total):
            nonlocal res
            
            if total == amount:
                res += 1
                return
            
            if i == len(coins) or total > amount:
                return
            
            # include num, don't increment i
            dfs(i, total + coins[i])
            
            # don't include num, increment i
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
        '''
        # approach 2: memoization
        
        dp = {}
        
        def dfs(i, remaining):
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            if remaining == 0:
                return 1
            
            if i == len(coins) or remaining < 0:
                return 0

            dp[(i, remaining)] = (dfs(i, remaining - coins[i]) + 
                                  dfs(i + 1, remaining))
            
            return dp[(i, remaining)]
            
        return dfs(0, amount)