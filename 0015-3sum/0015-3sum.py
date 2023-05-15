class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # approach: sort array, then twosum at each index
        
        res = []
        
        def twoSumII(i, l, r):
            num = nums[i]
            target = -num
            
            while l < r:
                sum = nums[l] + nums[r]

                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        nums.sort()
        length = len(nums)
        i = 0
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            twoSumII(i, i + 1, length - 1)
        
        return res