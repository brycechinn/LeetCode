class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach 1: nums -> min heap of size k, then top element is kth largest
        '''
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
        '''
    
        # approach 2: quick select
        k = len(nums) - k
        
        def quickSelect(l, r):
            p, pivot = l, nums[r]
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            
            if p < k:
                return quickSelect(p + 1, r)
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)
            
        