class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach: hashmap of num : index, indices must be different
        
        hashmap = {}
        
        for i, n in enumerate(nums):
            hashmap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in hashmap and i != hashmap[diff]:
                return [i, hashmap[diff]]