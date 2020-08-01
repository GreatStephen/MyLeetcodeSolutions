class Solution {
    public int countSubstrings(String s) {
        // a DP solution works in O(N2), not very fast, but very easy to DP
        int length = s.length();
        boolean[][] dp = new boolean[length][length];
        int res = 0;

        for(int len=1; len<=length; len++){
            for(int i=0; i<length; i++){
                int j = i+len-1;
                if(j>=length){
                    break;
                }                
                if(len==1){
                    dp[i][j] = true;
                    ++res;
                }
                else if(len==2){
                    dp[i][j] = (s.charAt(i)==s.charAt(j));
                    if(dp[i][j]){
                        ++res;
                    }
                }
                else{
                    dp[i][j] = (s.charAt(i)==s.charAt(j) && dp[i+1][j-1]);
                    if(dp[i][j]){
                        ++res;
                    }
                }
            }
        }

        return res;
    }
}