class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # approach: check rows, then columns, then sub-boxes
        
        def checkRows():
            for i in range(len(board)):
                found = set()

                for j in range(len(board)):
                    num = board[i][j]
                    
                    if num == '.':
                        continue
                        
                    if num in found:
                        return False
                    else:
                        found.add(num)
            return True
        
        def checkCols():
            for i in range(len(board)):
                found = set()
                
                for j in range(len(board)):
                    num = board[j][i]
                    
                    if num == '.':
                        continue
                        
                    if num in found:
                        return False
                    else:
                        found.add(num)
            return True
        
        def checkBox(row, col):
            found = set()
            
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    num = board[i][j]
                    
                    if num == '.':
                        continue
                        
                    if num in found:
                        return False
                    else:
                        found.add(num)
            return True
        
        def checkBoxes():
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    if not checkBox(i, j):
                        return False
            return True
                
        return checkRows() and checkCols() and checkBoxes()
        
        