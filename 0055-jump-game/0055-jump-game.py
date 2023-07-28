class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # approach: greedy
        
        if len(nums) == 1:
            return True
        
        prev = -1
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= prev:
                prev = i
        
        return prev == 0