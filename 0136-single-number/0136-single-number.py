class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # approach: xor each num, remaining num is result
        
        res = 0
        
        for num in nums:
            res = res ^ num
        
        return res