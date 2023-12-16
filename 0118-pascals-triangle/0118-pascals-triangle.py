class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        
        for i in range(numRows - 1):
            prev = res[-1]
            curr = []
            
            for i in range(len(prev) + 1):
                l = prev[i - 1] if i > 0 else 0
                r = prev[i] if i < len(prev) else 0
                
                curr.append(l + r)
            
            res.append(curr)
        
        return res