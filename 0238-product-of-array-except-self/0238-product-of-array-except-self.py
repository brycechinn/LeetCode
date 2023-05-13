class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # approach 1: make an array where each element is the product of all
        # other elements in the input array except itself
        
        '''
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            prod = 1
            
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            
            res[i] = prod
        
        return res
        '''
    
        # approach 2: two-pass array, first for prefix, second for postfix
        
        res = [1] * len(nums)
        pre = post = 1
        
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        for i in reversed(range(len(nums))):
            res[i] *= post
            post *= nums[i]
        
        return res
        