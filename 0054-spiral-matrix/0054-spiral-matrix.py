class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # approach: 4 pointers (l, r, t, b)
        
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n, 0, m
        
        res = []
        
        while l < r and t < b:
            # top row
            for i in range(l, r):
                res.append(matrix[t][i])
            
            t += 1
            
            # right column
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            
            r -= 1
            
            if not (l < r and t < b):
                break
            
            # bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            
            b -= 1
            
            # left column
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
                
            l += 1
    
        return res