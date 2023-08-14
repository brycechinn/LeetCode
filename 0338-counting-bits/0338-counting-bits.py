class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n + 1)
        
        for i in range(n, -1, -1):
            res[i] = self.countOnes(i)
        
        return res
    
    def countOnes(self, n):
        res = 0
        
        while n:
            res += n % 2
            n = n >> 1
        
        return res