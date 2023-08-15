class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # approach: hashset of seen nums
        
        seen = set()
        
        for n in nums:
            if n in seen:
                return True
            
            seen.add(n)
        
        return False