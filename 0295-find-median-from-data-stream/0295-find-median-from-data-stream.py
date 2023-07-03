class MedianFinder:
# approach 1: insert in order

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        for i, n in enumerate(self.nums):
            if num <= n:
                self.nums.insert(i, num)
                return
        
        self.nums.append(num)

    def findMedian(self) -> float:
        if len(self.nums) % 2:
            i = len(self.nums) // 2
            return float(self.nums[i])
        else:
            l = len(self.nums) // 2 - 1
            r = l + 1
            return float((self.nums[l] + self.nums[r]) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()