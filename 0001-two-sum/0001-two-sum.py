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
            
            if diff in d:
                return [i, d[diff]]
            else:
                d[num] = i