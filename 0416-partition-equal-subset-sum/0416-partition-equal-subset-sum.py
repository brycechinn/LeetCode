class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # approach 1: backtracking DFS, include num in left partition or don't
        # (i.e. include in right partition)
        '''
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        res, part = [], []
        
        def dfs(i, total):
            if i == len(nums) or total > target:
                return
            
            if total == target:
                res.append(part.copy())
                return
            
            num = nums[i]
            
            part.append(num)
            dfs(i + 1, total + num)
            
            # backtrack
            part.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return len(res) > 0
        '''
        # approach 2: bottom-up DP via backwards iteration, set of all
        # possible sums
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        
        sums = set()
        sums.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            
            for s in sums.copy():
                sums.add(s + n)
                
                if target in sums:
                    return True
        
        return False