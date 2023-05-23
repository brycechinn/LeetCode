class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # approach 1: start with k = min(piles), increment k until
        # time <= h
        
        '''
        k = 1
        total = float(inf)
    
        while total > h:
            total = 0
            for pile in piles:
                hours = ceil(pile / k)
                total += hours

            if total > h:
                k += 1
        
        return k
        '''
    
        # approach 2: optimize brute force with binary search on 
        # range [1, max(piles)]
        
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            
            total = 0
            for pile in piles:
                hours = ceil(pile / k)
                total += hours

            if total <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res