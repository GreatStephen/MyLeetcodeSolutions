class TicTacToe {
    private int[] row;
    private int[] col;
    private int diag;
    private int anti_diag;
    private int res;
    private int N;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        row = new int[n];
        Arrays.fill(row, n);
        col = new int[n];
        Arrays.fill(col, n);
        diag = n;
        anti_diag = n;
        res = -1;
        N = n;
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        // already have a result
        if(res!=-1) return res;

        int val = player==1?1:-1;

        // update the sum of each row, each col, diag and anti-diag
        // sum=0 -> player2 wins, sum=2n -> player1 wins
        this.row[row] += val;
        if(this.row[row]==0) res = 2;
        else if(this.row[row]==2*N) res = 1;

        this.col[col] += val;
        if(this.col[col]==0) res = 2;
        else if(this.col[col]==2*N) res = 1;

        if(row==col){
           this.diag += val; 
           if(this.diag==0) res = 2;
           else if(this.diag==2*N) res = 1;
        } 

        if(row+col==N-1){
            this.anti_diag += val;
            if(this.anti_diag==0) res = 2;
            else if(this.anti_diag==2*N) res = 1;
        } 

        return res==-1?0:res;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */