class Solution:
    def rob(self, nums: List[int]) -> int:
        # approach: call houseRobberI for nums[1:], nums[:-1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        one, two = 0, nums[0]
        
        for i in range(1, len(nums)):
            new = max(two, nums[i] + one)
            one = two
            two = new
        
        return two