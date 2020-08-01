class Solution {
    public void gameOfLife(int[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        int[] neighbors = {0, 1, -1};
        
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                int live_neighbor = 0;
                
                // count the live neighbors
                for(int ni=0; ni<3; ni++){
                    for(int nj = 0; nj<3; nj++){
                        if(ni==0 && nj==0) continue;
                        int r = (i + neighbors[ni]);
                        int c = (j + neighbors[nj]);
                        
                        if(r>=0 && r<rows && c>=0 && c<cols)
                            if(board[r][c]==1 || board[r][c]==-1)
                                live_neighbor++;
                        
                    }
                }
                // System.out.println(live_neighbor);
                
                // apply the rules
                if(live_neighbor <=1)
                    board[i][j] = board[i][j]==1?-1:0;
                else if(live_neighbor ==2)
                    board[i][j] = board[i][j]==1?1:0;
                else if(live_neighbor ==3)
                    board[i][j] = board[i][j]==1?1:2;
                else 
                    board[i][j] = board[i][j]==1?-1:0;
            }
        }
        
        // get the result matrix
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                board[i][j] = board[i][j]==2?1:board[i][j];
                board[i][j] = board[i][j]==-1?0:board[i][j];
            }
        }
    }
}