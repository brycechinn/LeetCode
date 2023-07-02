class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # approach: points -> distances from origin -> min heap
        
        hashmap = collections.defaultdict(list)
        dists, res = [], []
        
        for p in points:
            d = math.sqrt((p[0] * p[0]) + (p[1] * p[1]))
            dists.append(d)
            hashmap[d].append(p)
        
        heapq.heapify(dists)
        
        for _ in range(k):
            d = heapq.heappop(dists)
            res.append(hashmap[d].pop())
        
        return res
        
            