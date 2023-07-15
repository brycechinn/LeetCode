class Solution:
    def climbStairs(self, n: int) -> int:
        # approach 1: DFS (TLE)
        
        # time: O(2^n)
        # space: O(1)
        
        '''
        res = 0
        
        def dfs(steps):
            nonlocal res
            
            if steps > n:
                return
            
            if steps == n:
                res += 1
                return
            
            dfs(steps + 1)
            dfs(steps + 2)
        
        dfs(0)
        return res
        '''
        
        # approach 2: bottom-up DP with memoization table
        
        '''
        # time: O(n)
        # space: O(n)
        memo = [1] * (n + 1)
        
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[-1]
        '''
        
        # approach 3: bottom-up DP with one and two variables
        
        # time: O(n)
        # space: O(1)

        one = 1
        two = 1
        
        for i in range(n - 1):
            i = one + two
            two = one
            one = i
        
        return one