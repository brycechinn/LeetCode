class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # approach: Bellman-Ford

        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tmp = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                    
                if prices[s] + p < tmp[d]:
                    tmp[d] = prices[s] + p
                    
            prices = tmp
        
        return prices[dst] if prices[dst] != float('inf') else -1
            
            