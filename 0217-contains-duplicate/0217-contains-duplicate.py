class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 1:
            return False
        
        seen = set()
        res = False
        
        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False
        