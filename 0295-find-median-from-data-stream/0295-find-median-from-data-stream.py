class MedianFinder:
    # approach: maxheap for left portion, minheap for right portion

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -1 * num)
        
        # make sure left nums < right nums
        if self.left and self.right and -1 * self.left[0] > self.right[0]:
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        
        # balance heaps
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, -1 * heapq.heappop(self.left))
            else:
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        
        if len(self.left) < len(self.right):
            return self.right[0]
        
        return ((-1 * self.left[0]) + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()