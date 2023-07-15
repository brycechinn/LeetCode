class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # approach 1: DFS (TLE)
        '''
        cost.insert(0, 0)
        n = len(cost)
        res = float('inf')

        def dfs(i, total):
            nonlocal res
            
            if i > n:
                return
            
            if i == n:
                res = min(res, total)
                return
            
            total += cost[i]
            
            dfs(i + 1, total)
            dfs(i + 2, total)
        
        dfs(0, 0)
        return res
        '''
        
        # approach 2: bottom-up DP
        cost.insert(0, 0)
        n = len(cost)
        one, two = cost[-1], 0
        
        for i in range(n - 2, -1, -1):
            new = min(cost[i] + one, cost[i] + two)
            two = one
            one = new
        
        return one
            
            