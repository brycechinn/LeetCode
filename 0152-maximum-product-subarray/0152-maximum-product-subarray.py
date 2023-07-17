class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # approach: bottom-up DP via iteration, sml and lrg variables

        sml, lrg = 1, 1
        res = max(nums)
        
        for i in range(len(nums) - 1, -1, -1):        
            num = nums[i]
            
            if num == 0:
                sml, lrg = 1, 1
                continue
            
            tmp = sml
            sml = min(num * sml, num * lrg, num)
            lrg = max(num * tmp, num * lrg, num)
            res = max(res, lrg)

        return res