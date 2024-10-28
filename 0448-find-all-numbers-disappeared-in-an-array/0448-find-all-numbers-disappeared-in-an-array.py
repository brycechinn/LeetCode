class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        # approach 1: hashset to track missing nums
        # time: O(n) space: O(n)
        
        missing = set(range(1, len(nums) + 1))
        
        for num in nums:
            if num in missing:
                missing.remove(num)
                
        return list(missing)
        '''
        
        # approach 2: map indices to values and mark existing as negative
        # time: O(n) space: O(1)
        
        for i, num in enumerate(nums):
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])
        
        return [ i + 1 for i, num in enumerate(nums) if num > 0 ]