class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: max heap, pop k - 1 times
        
        heap = []
        for n in nums:
            heapq.heappush(heap, -1 * n)
            
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -1 * heap[0]