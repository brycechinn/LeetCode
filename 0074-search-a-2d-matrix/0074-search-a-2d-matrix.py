class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approach: binary search to find row, then binary search
        # to find num within row
        
        l = 0
        r = len(matrix) - 1
        m = 0
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
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l + r) // 2
            
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        
        return False