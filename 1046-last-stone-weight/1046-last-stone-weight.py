class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # approach: max heap, pop two nums at a time
        
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, -1 * abs(x - y))
        
        return -1 * stones[0] if stones else 0