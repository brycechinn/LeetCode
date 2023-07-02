class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: nums -> min heap of size k, then top element is kth largest
        
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]