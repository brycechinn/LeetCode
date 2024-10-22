class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        # approach 1: dictionary of num count
        
        d, n = defaultdict(int), len(nums)
        
        for num in nums:
            d[num] += 1
            
            if d[num] > n // 2:
                return num
        
        # unreachable given constraints
        return 0
        '''
    
        # approach 2: O(1) space solution
        majority, count = nums[0], 0
        
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            else:
                if num == majority:
                    count += 1
                else:
                    count -= 1
        
        return majority
        