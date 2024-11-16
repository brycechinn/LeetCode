class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # approach 1: brute force
        # time: O(n^2), space: O(1)
        
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    res += 1
        
        return res