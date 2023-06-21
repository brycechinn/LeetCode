class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(nums):
            hashmap[num] = i
            
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashmap and i != hashmap[diff]:
                return [i, hashmap[diff]]