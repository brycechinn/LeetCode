class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # approach 1: top-down DP via memoization with cache of 
        # (i, total) : unique combinations

        dp = {}
        
        def dfs(i, remaining):
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            
            if i == len(coins) or remaining < 0:
                return 0
            
            if remaining == 0:
                return 1

            dp[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return dp[(i, remaining)]
        
        return dfs(0, amount)