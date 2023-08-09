class Solution:
    def isHappy(self, n: int) -> bool:
        # approach: hashset of seen nums, loop until n == 1 or duplicate found
        
        visited = set()
        
        while n != 1:
            if n in visited:
                return False
            
            visited.add(n)
            total = 0
            
            for c in str(n):
                d = int(c)
                total += d * d
                
            n = total
                
        return True