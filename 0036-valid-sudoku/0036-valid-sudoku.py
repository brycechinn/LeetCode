class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # approach: check rows, then cols, then sub-boxes
        
        def checkBox(row_start, col_start):   
            hashset = set()

            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    n = board[i][j]

                    if n != '.':
                        if n in hashset:
                            return False
                        
                        hashset.add(n)

            return True
        
        row_hash = collections.defaultdict(set)
        col_hash = collections.defaultdict(set)
        
        # check rows and cols
        for i in range(len(board)):
            for j in range(len(board)):
                r = board[i][j]
                c = board[j][i]
                
                if (r != '.'):
                    if r in row_hash[i]:
                        return False
                    
                    row_hash[i].add(r)
                
                if (c != '.'):
                    if c in col_hash[i]:
                        return False
                    
                    col_hash[i].add(c)
        
        # check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checkBox(i, j):
                    return False
        
        return True
                