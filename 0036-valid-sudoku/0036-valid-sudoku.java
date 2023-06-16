class Solution {
    public boolean isValidSudoku(char[][] board) {
        // approach: hashset of seen nums, check rows, then cols, the sub-boxes
        
        int size = board[0].length;
        
        // check rows and cols
        for (int i = 0; i < size; i++) {            
            Set<Character> rowSet = new HashSet<>();
            Set<Character> colSet = new HashSet<>();

            for (int j = 0; j < size; j++) {
                char r = board[i][j];
                char c = board[j][i];
                
                if (r != '.') {
                    if (rowSet.contains(r)) {
                        return false;
                    }

                    rowSet.add(r);
                }
                
                if (c != '.') {
                    if (colSet.contains(c)) {
                        return false;
                    }

                    colSet.add(c);
                }
            }
        }
        
        // check boxes
        int startI = 3;
        int startJ = 0;
        
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                if (!checkBox(board, i, j)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean checkBox(char[][] board, int startI, int startJ) {
        Set<Character> boxSet = new HashSet<>();
        
        for (int i = startI; i < startI + 3; i++) {
            for (int j = startJ; j < startJ + 3; j++) {
                char n = board[i][j];
                
                System.out.println(board[i][j]);
                
                if (n != '.') {
                    if (boxSet.contains(n)) {
                        return false;
                    }
                    
                    boxSet.add(n);
                }
            }
        }
        
        return true;
    }
}