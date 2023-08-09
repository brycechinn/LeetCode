class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # approach 1: store rows and cols to zero in sets
        # time: O(mn)
        # space: O(m + n)
        '''
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        
        for r in rows:
            for c in range(n):
                matrix[r][c] = 0
        
        for c in cols:
            for r in range(m):
                matrix[r][c] = 0    
        '''
        
        # approach 2: store rows and cols to zero in matrix itself,
        # use a single variable to represent row zero
        # time: O(mn)
        # space: O(1)
        
        m, n = len(matrix), len(matrix[0])
        row_zero = False
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(n):
                matrix[0][c] = 0