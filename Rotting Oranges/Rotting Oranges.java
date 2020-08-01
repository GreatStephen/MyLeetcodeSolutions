class Solution {
    public int orangesRotting(int[][] grid) {
        ArrayList<ArrayList<Integer>> queue = new ArrayList<ArrayList>>();
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[].length; j++){
                ArrayList<Integer> rotten = new ArrayList<>(){
                    add(i);
                    add(j);
                }
                queue.add(rotten);
            }
        }
        while(queue.size()!=0){
            ArrayList<Integer> rotten = queue.get(0);
            queue.remove(0);
            int row = rotten.get(0);
            int col = rotten.get(1);
            if(row-1>=0 && grid[row-1][col]==1){
                grid[row-1][col]=2;
                ArrayList<Integer> new_rotten = new ArrayList<>(){
                    add(row-1);
                    add(col);
                }
                queue.add(new_rotten);
            } 
            if(row+1<grid[].length && grid[row+1][col]==1) grid[row+1][col]=2;
            if(col-1>=0 && grid[row][col-1]==1) grid[row][col-1]=2;
            if(col+1<grid[].length && grid[row][col+1]==1) grid[row][col+1]=2;
        }
    }
}