class Solution {
    // increasing number
    int[][] memo;
    
    public int longestIncreasingPath(int[][] matrix) {
        // DFS + memo, memo[i][j] records the answer for this point
        if(matrix.length==0) return 0;
        int R = matrix.length;
        int C = matrix[0].length;
        int ans=0;
        memo = new int[R][C];

        for(int i=0; i<R; i++){
            Arrays.fill(memo[i], -1);
        }
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                int temp_max = DFS(matrix, i, j);
                ans = Math.max(ans, temp_max);
            }
        }
        
        // for(int i=0; i<R; i++){
        //     System.out.println(Arrays.toString(memo[i]));
        // }
        

        return ans;
    }

    private int DFS(int[][] matrix, int r, int c){
        if(memo[r][c]!=-1){
            // if(memo[r][c]>ans) ans = memo[r][c];
            return memo[r][c];
        }

        int temp_max = 1;
        // up, right, down, left
        int[] r_offset = new int[]{-1,0,1,0};
        int[] c_offset = new int[]{0,1,0,-1};

        for(int i=0; i<4; i++){
            int new_r = r+r_offset[i];
            int new_c = c+c_offset[i];
            if(new_r>=0 && new_r<matrix.length && new_c>=0 && new_c<matrix[0].length){
                if(matrix[new_r][new_c]>matrix[r][c]){
                    int next_max = DFS(matrix, new_r, new_c);
                    temp_max = Math.max(temp_max, next_max+1);
                }
            }
        }
        // if(r==0 && c==2) System.out.println(temp_max);

        memo[r][c] = temp_max;
        return temp_max;
    }
}