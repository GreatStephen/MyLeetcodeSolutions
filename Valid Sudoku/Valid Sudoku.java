class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 1-pass traversal
        HashMap<Character, Integer>[] row = new HashMap[9];
        HashMap<Character, Integer>[] col = new HashMap[9];
        HashMap<Character, Integer>[] box = new HashMap[9];

        for(int i=0; i<9; i++){
            row[i] = new HashMap();
            col[i] = new HashMap();
            box[i] = new HashMap();
        }

        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j]=='.') continue;

                if(row[i].containsKey(board[i][j])) return false;             
                else row[i].put(board[i][j], 1);

                if(col[j].containsKey(board[i][j])) return false;
                else col[j].put(board[i][j], 1);

                int box_index = (i/3)*3+j/3;
                if(box[box_index].containsKey(board[i][j])) return false;
                else box[box_index].put(board[i][j], 1);
            }
        }
        return true;

    }

}