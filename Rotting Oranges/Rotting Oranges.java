class Solution {
    public int orangesRotting(int[][] grid) {
        int level=0;
        ArrayList<ArrayList<Integer>> queue = new ArrayList<ArrayList<Integer>>();
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==2){
                    ArrayList<Integer> list = new ArrayList<Integer>();
                    list.add(i);
                    list.add(j);
                    list.add(0);
                    queue.add(list);
                }
            }
        }
        while(queue.size()!=0){
            ArrayList<Integer> rotten = queue.get(0);
            queue.remove(0);
            int row = rotten.get(0);
            int col = rotten.get(1);
            int temp_level = rotten.get(2);
            level=Math.max(level, temp_level);
            if(row-1>=0 && grid[row-1][col]==1){
                grid[row-1][col]=2;
                ArrayList<Integer> temp_node = new ArrayList<>(){
                    {
                        add(row-1);
                        add(col);
                        add(temp_level+1);
                    }
                    
                };
                queue.add(temp_node);
            } 
            if(row+1<grid.length && grid[row+1][col]==1){
                grid[row+1][col]=2;
                queue.add(new ArrayList<>(){
                    {
                        add(row+1);
                        add(col);
                        add(temp_level+1);
                    }
                    
                });
            } 
            if(col-1>=0 && grid[row][col-1]==1){
                grid[row][col-1]=2;
                queue.add(new ArrayList<>(){
                    {
                        add(row);
                        add(col-1);
                        add(temp_level+1);
                    }
                    
                });
            } 
            if(col+1<grid[0].length && grid[row][col+1]==1){
                grid[row][col+1]=2;
                queue.add(new ArrayList<>(){
                    {
                        add(row);
                        add(col+1); 
                        add(temp_level+1);
                    }
                    
                });
            } 
        }
        
        for(int[] i:grid){
            for(int j:i){
                if(j==1) return -1;
            }
        }
        return level;
    }
}