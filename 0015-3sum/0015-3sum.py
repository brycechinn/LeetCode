class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # approach: sort array, then twosum at each index
        
        res = []
        
        def twoSumII(num, l, r):            
            while l < r:
                sum = num + nums[l] + nums[r]

                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        nums.sort()
        length = len(nums)
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            twoSumII(num, i + 1, length - 1)
        
        return res