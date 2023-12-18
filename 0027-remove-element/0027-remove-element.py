class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) == 0:
            return 0
        
        count = 0
        for num in nums:
            if num == val:
                count += 1
        
        res = len(nums) - count
        ptr = len(nums) - 1
        
        for i in range(len(nums)):
            if ptr == i:
                return res
            
            while nums[i] == val:
                # swap curr num and ptr num
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr -= 1
                
                if ptr == i:
                    return res
            
        return res
                