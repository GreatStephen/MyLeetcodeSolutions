class Solution {
    public boolean isMatch(String s, String p) {
        // DP solution
        int i = s.length();
        int j = p.length();
        boolean[][] dp = new boolean[i+1][j+1];
        dp[i][j] = true;
        for(i=0; i<s.length(); i++){
            dp[i][p.length()] = false;
        }

        for(i=s.length(); i>=0; i--){
            for(j=p.length()-1; j>=0; j--){
                // the first letter matches or not
                boolean first_match = i<s.length() && (s.charAt(i)==p.charAt(j) || p.charAt(j)=='.');

                // if the second letter is *
                if(j+1<p.length() && p.charAt(j+1)=='*'){
                    // never repeat || repeat 1 or more times
                    dp[i][j] = dp[i][j+2] || ((i+1<=s.length()?dp[i+1][j]:false) && first_match);
                    // if(i==7 && j==7){
                    //     System.out.println(dp[i][j+2] || (dp[i+1][j] && first_match));
                    //     System.out.println(first_match);
                    //     System.out.println((i+1<=s.length()?dp[i+1][j]:false) && first_match);
                    // }
                }
                else{
                    dp[i][j] = first_match && dp[i+1][j+1];
                }
                // System.out.println(dp[i][j]);
            }
        }

        return dp[0][0];
    }
}