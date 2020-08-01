class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m+1][n+1];

        // initialize
        for(int i=0; i<=m; i++){
            dp[i][0] = i;
        }
        for(int j=0; j<=n; j++){
            dp[0][j] = j;
        }

        // fill the dp array
        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                // left
                int a = dp[i][j-1]+1;
                // up
                int c = dp[i-1][j]+1;  
                int b = 0;  
                if(word1.charAt(i-1) == word2.charAt(j-1)){
                    // left-up
                    b = dp[i-1][j-1];                    
                }
                else{
                    // left-up
                    b = dp[i-1][j-1]+1;
                }
                int min = 0;
                if(a<=b && a<=c){
                    min = a;
                }
                else if(b<=a && b<=c){
                    min = b;
                }
                else{
                    min = c;
                }
                dp[i][j] = min;
            }
        }

        return dp[m][n];
    }
}