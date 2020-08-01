class Solution {
    public boolean isMatch(String s, String p) {
        int R = p.length(), C = s.length();
        boolean[][] dp = new boolean[R+1][C+1];

        // initialize
        for(int i=0; i<R+1; i++){
            if(i==0) dp[i][0] = true;
            else{
                if(p.charAt(i-1)=='*'){
                    dp[i][0] = dp[i-1][0];
                }
            } 
        }
        for(int j=1; j<C+1; j++){
            dp[0][j] = false;
        }

        // traverse
        for(int i=1; i<R+1; i++){
            for(int j=1; j<C+1; j++){
                char p_char = p.charAt(i-1);
                char s_char = s.charAt(j-1);

                if(p_char=='*'){
                    if(dp[i-1][j]) dp[i][j] = true;
                    else{
                        int t=0;
                        for(t=j-1; t>=0; t--){
                            if(dp[i][t]==true){
                                dp[i][j] = true;
                                break;
                            }
                        }
                        if(t<0) dp[i][j] = false;
                    }
                }
                else if(p_char=='?'){
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    if(p_char!=s_char) dp[i][j] = false;
                    else dp[i][j] = dp[i-1][j-1];
                }
            }
        }

        return dp[R][C];
    }
}