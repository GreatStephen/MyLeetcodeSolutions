class Solution {
    public int numIslands(char[][] grid) {
        int num=0;
        int row=grid.length;
        int col=grid[].length;
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(grid[i][j]=='1'){
                    DFS(grid, i, j);
                    num++;
                }
            }
        }
        return num;
    }

    public void DFS(char[][] grid, int i, int j){
        int row=grid.length;
        int col=grid[].length;
        if(grid[i][j]=='1') grid[i][j]='0';
        if(i-1>=0 && grid[i-1][j]=='1') DFS(grid, i-1, j);
        if(i+1<=row && grid[i+1][j]=='1') DFS(grid, i+1, j);
        if(j-1>=0 && grid[i][j-1]=='1') DFS(grid, i, j-1);
        if(j+1>=0 && grid[i][j+1]=='1') DFS(grid, i, j+1);
    }
}