class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # approach: hashmap
        
        d = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff not in d:
                d[num] = i
            else:
                return [i, d[diff]]