class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[][] f = new int[n+1][m+1];
        int[] sub = new int[n+1];
        
        for(int[] row : f)
            Arrays.fill(row, Integer.MAX_VALUE);
        
        for(int i=1; i<=n; i++)
            sub[i] = sub[i-1] + nums[i-1];
        
        f[0][0]=0;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                for(int k=0; k<i; k++){
                    f[i][j] = Math.min(f[i][j], Math.max(f[k][j-1], sub[i]-sub[k]));
                }
            }
        }
        return f[n][m];
        
        }
}