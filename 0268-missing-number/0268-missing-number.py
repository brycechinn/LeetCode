class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # approach: arithmetic series
        
        n = len(nums)
        total = (n * (n + 1)) // 2
        return total - sum(nums)