class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach: hashset of starts of sequences, then iterate from each start
        
        if not nums:
            return 0
        
        numset = set(nums)
        starts = []
        longest = 0
        
        for num in nums:
            if num - 1 not in numset:
                starts.append(num)
                
        for start in starts:
            num = start
            length = 1
            
            while (num + 1 in numset):
                length += 1
                num = num + 1
        
            longest = max(longest, length)
        
        return longest