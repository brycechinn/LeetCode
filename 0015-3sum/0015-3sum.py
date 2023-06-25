class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # approach: sort nums, then two sum II at each index
        
        result = []
        
        def twoSumII(i):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            
            print(i, l, r, target)
            
            while l < r:
                left = nums[l]
                right = nums[r]
                
                total = left + right
                
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            twoSumII(i)
        
        return result
            