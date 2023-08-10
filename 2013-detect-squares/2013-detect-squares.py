class DetectSquares:
    # approach: hashmap of point : count, list of points, look for diagonal points, 
    # then check if corners exist in hashmap

    def __init__(self):
        self.counts, self.points = {}, []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] = 1 + self.counts.get(tuple(point), 0)
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        
        for x2, y2 in self.points:
            if abs(x2 - x1) != abs(y2 - y1) or x1 == x2 or y1 == y2:
                continue
                
            if (x1, y2) in self.counts and (x2, y1) in self.counts:
                res += self.counts[(x1, y2)] * self.counts[(x2, y1)]
        
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)