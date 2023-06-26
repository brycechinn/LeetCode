class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # approach: binary search on range [1, max(piles)]
        
        result = float('inf')
        l = 1
        r = max(piles)
        while l <= r:
            m = (l + r) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)

            if hours > h:
                l = m + 1
            else:
                r = m - 1
                
                # potential new min k
                result = min(result, m)
        
        return result