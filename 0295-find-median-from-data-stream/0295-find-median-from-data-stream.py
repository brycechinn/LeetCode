class MedianFinder:
    # approach: maxheap for left portion, minheap for right portion
    
    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        # default add to left
        heapq.heappush(self.left, -1 * num)
        
        if ((len(self.left) - len(self.right) > 1) or 
            (self.right and (-1 * self.left[0]) > self.right[0])):
                
            # move left max to right
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
            
            if len(self.right) - len(self.left) > 1:
                # move right min to left
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (-1 * self.left[0] + self.right[0]) / 2
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()