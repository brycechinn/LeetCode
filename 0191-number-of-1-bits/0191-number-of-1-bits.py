class Solution:
    def hammingWeight(self, n: int) -> int:
        # approach: while num > 0, num % 2, then right shift
        
        res = 0
        
        while n:
            res += n % 2
            n = n >> 1
        
        return res