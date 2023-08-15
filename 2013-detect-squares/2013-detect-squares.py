class DetectSquares:
    # approach: list of points, hashmap of points

    def __init__(self):
        self.points = []
        self.counts = {}

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.counts[tuple(point)] = 1 + self.counts.get(tuple(point), 0)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0
        
        for x2, y2 in self.points:
            if abs(x1 - x2) != abs(y1 - y2) or x1 == x2 or y1 == y2:
                continue
                
            if (x1, y2) in self.counts and (x2, y1) in self.counts:
                total += self.counts[(x1, y2)] * self.counts[(x2, y1)]
        
        return total

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)