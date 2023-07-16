class Solution:
    def rob(self, nums: List[int]) -> int:
        # approach: bottom-up DP via iteration, one and two variables
        
        one, two = 0, nums[0]
        
        for i in range(1, len(nums)):
            new = max(two, nums[i] + one)
            one = two
            two = new
        
        return two