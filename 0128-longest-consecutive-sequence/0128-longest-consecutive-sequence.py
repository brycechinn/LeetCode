class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # approach: set from input array, then find starting values of sequences
        # -> iterate from each starting value until the sequence is broken
        
        if not nums:
            return 0
        
        s, res = set(nums), 1
        
        for num in nums:
            if (num - 1) in s:
                continue
            
            curr = 0
            
            while num + curr in s:
                curr += 1
            
            res = max(res, curr)
            
        return res
                
                
                
                
            
            
            
            