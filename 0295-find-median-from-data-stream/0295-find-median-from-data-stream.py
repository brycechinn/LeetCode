class MedianFinder:
    # approach: maxheap for left portion, minheap for right portion

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.left, -1 * num)
        elif not self.left:
            if num <= self.right[0]:
                heapq.heappush(self.left, -1 * num)
            else:
                heapq.heappush(self.right, num)
        elif not self.right:
            if num >= -1 * self.left[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -1 * num)
        else:
            if num <= self.right[0]:
                heapq.heappush(self.left, -1 * num)
            else:
                heapq.heappush(self.right, num)

        while abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, -1 * heapq.heappop(self.left))
            else:
                heapq.heappush(self.left, -1 * heapq.heappop(self.right))

    def findMedian(self) -> float:
        if abs(len(self.left) - len(self.right)) == 1:
            if len(self.left) > len(self.right):
                return -1 * self.left[0]
            else: 
                return self.right[0]
        else:
            return ((-1 * self.left[0]) + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()