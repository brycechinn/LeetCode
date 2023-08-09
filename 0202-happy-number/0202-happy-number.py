class Solution:
    def isHappy(self, n: int) -> bool:
        # approach: hashset of seen nums, loop until n == 1 or duplicate found
        
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            total = 0
            
            for c in str(n):
                d = int(c)
                total += d * d
                
            n = total
                
        return True