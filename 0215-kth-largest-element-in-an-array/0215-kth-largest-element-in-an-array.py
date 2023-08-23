class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: min heap of size k
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]