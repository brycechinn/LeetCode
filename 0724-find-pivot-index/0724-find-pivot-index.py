class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # approach: use sum of nums to calculate left and right sum
        # time: O(n)
        # space: O(1)
        
        left_sum, right_sum = 0, sum(nums)
        
        for i, num in enumerate(nums):
            right_sum -= num
            
            if left_sum == right_sum:
                return i
            
            left_sum += num
            
        return -1