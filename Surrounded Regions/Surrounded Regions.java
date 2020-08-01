class Solution {
    public void solve(char[][] board) {
        int R = board.length;
        int C = board[0].length;

        // DFS on the border
        for(int i=0; i<R; i++){
            if(board[i][0]=='O')
                DFS(board, i, 0);
            if(board[i][C-1]=='O')
                DFS(board, i, C-1);
        }
        for(int j=1; j<=C-2; j++){
            if(board[0][j]=='O')
                DFS(board, 0, j);
            if(board[R-1][j]=='O')
                DFS(board, R-1, j);
        }

        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                if(board[i][j]=='X') continue;
                if(board[i][j]=='#') board[i][j]='O';
                else if(board[i][j]=='O') board[i][j]='X';
            }
        }
    }

    private void DFS(char[][] board, int r, int c){
        board[r][c] = '#';

        int[] r_offset = new int[]{-1,0,1,0};
        int[] c_offset = new int[]{0,1,0,-1};
        for(int i=0; i<4; i++){
            int new_r = r+r_offset[i];
            int new_c = c+c_offset[i];
            if(new_r>=0 && new_r<board.length && new_c>=0 && new_c<board[0].length){
                if(board[new_r][new_c]=='O'){
                    DFS(board, new_r, new_c);
                }
            }
        }
    }
}