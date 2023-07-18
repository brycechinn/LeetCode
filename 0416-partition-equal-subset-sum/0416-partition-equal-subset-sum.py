class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # approach 1: backtracking DFS to generate all possible 
        # left and right partitions
        '''
        res = False
        
        def dfs(i, left, right):
            nonlocal res
            
            if i == len(nums):
                if sum(left) == sum(right):
                    res = True
                return

            left.append(nums[i])
            dfs(i + 1, left, right)
            left.pop()
            
            right.append(nums[i])
            dfs(i + 1, left, right)
            right.pop()

        dfs(0, [], [])
        return res
        '''
        # approach 2: backtracking DFS to find all partitions that
        # sum to sum(nums) / 2
        '''
        if sum(nums) % 2:
            return False
        
        target = sum(nums) / 2
        res = False
        
        def dfs(i, part):
            nonlocal res, target

            if i == len(nums):
                if sum(part) == target:
                    res = True
                return

            part.append(nums[i])
            dfs(i + 1, part)
            
            # backtrack
            part.pop()
            dfs(i + 1, part)
        
        dfs(0, [])
        return res
        '''
        # approach 3: bottom-up DP via backwards iteration, set of all possible 
        # sums, check if sum(nums) / 2 exists in set
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) / 2
        sums = set()
        sums.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            
            for s in list(sums):
                sums.add(n + s)
            
            sums.add(n)
            
            if target in sums:
                return True
        
        return False
                
        
        