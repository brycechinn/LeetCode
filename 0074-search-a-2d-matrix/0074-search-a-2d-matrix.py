class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approach: two binary searches, one to find row and one to
        # find num within row
        
        l, r, m = 0, len(matrix) - 1, 0
        
        while l <= r:
            m = (l + r) // 2
            row = matrix[m]
            
            if target > row[-1]:
                l = m + 1
            elif target < row[0]:
                r = m - 1
            else:
                break
        
        row = matrix[m]
        l, r = 0, len(row) - 1
        
        while l <= r:
            m = (l + r) // 2
            num = row[m]
            
            if target > num:
                l = m + 1
            elif target < num:
                r = m - 1
            else:
                return True
        
        return False