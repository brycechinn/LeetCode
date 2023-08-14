class Solution:
    def reverseBits(self, n: int) -> int:
        # approach: add each bit to res, starting at the last bit, by using OR
        
        res = 0
        
        for i in range(32):
            bit = n & 1
            res = res | (bit << (31 - i))
            n = n >> 1
        
        return res