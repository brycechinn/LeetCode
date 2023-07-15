class Solution:
    def climbStairs(self, n: int) -> int:
        # approach: botom-up DP
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
        
        one = 1
        two = 1
        
        for i in range(n - 1):
            i = one + two
            two = one
            one = i
        
        return one