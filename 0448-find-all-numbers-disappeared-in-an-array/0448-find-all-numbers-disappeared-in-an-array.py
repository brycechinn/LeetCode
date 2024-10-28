class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # approach 1: hashset to track seen nums
        # time: O(n) space: O(n)
        
        missing = set(range(1, len(nums) + 1))
        
        for num in nums:
            if num in missing:
                missing.remove(num)
        
        return list(missing)