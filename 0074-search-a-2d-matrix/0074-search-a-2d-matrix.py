class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # approach 1: add nums to list then binary search
        
        '''
        nums = [num for row in matrix for num in row]
         
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        
        return False
        '''
    
        # approach 2: two binary searches, one to find row and one to find
        # num within row
        
        top, bot = 0, len(matrix) - 1
        row = []
        
        while top <= bot:
            mid = (top + bot) // 2
            
            row = matrix[mid]
            
            if row[-1] < target:
                top = mid + 1
            elif row[0] > target:
                bot = mid - 1
            else:
                break
    
        if top > bot:
            return False
        
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        
        return False
        
        