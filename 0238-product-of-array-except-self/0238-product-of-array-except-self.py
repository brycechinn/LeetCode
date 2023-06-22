class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach: prefix and postfix lists
        
        length = len(nums)
        prefix = [0] * length     
        pre = 1
        
        for i in range(length):
            prefix[i] = pre
            pre *= nums[i]
        
        postfix = [0] * length
        post = 1
        
        for i in reversed(range(length)):
            postfix[i] = post
            post *= nums[i]
        
        result = [0] * length
        
        for i in range(length):
            result[i] = prefix[i] * postfix[i]
        
        return result
        
        