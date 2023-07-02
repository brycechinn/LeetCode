class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # approach: points -> distances from origin -> min heap of [distance, x, y]

        heap, res = [], []
        
        for p in points:
            d = math.sqrt((p[0] * p[0]) + (p[1] * p[1]))
            heap.append([d, p[0], p[1]])

        heapq.heapify(heap)
        
        for _ in range(k):
            d, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res