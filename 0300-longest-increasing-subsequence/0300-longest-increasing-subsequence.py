class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # approach: bottom-up DP via backwards iteration, tabulation of
        # i : longest increasing subsequence from nums[i]
        
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        
        for i in range(len(nums) - 2, -1, -1):
            candidates = [1]
            
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    candidates.append(1 + dp[j])
            
            dp[i] = max(candidates)

        return max(dp)