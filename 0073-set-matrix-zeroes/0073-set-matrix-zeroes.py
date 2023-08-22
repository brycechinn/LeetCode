class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # approach: arrays two arrays to store rows/cols to be zeroed,
        # optimize by embedding arrays in matrix with extra left corner
        # variable
        
        m, n = len(matrix), len(matrix[0])
        
        rows, cols = [False] * m, [False] * n
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(m):
            if rows[r]:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if cols[c]:
                for r in range(m):
                    matrix[r][c] = 0