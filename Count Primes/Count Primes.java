class Solution {
    public int countPrimes(int n) {
        // fill a dp[] from a non-prime number
        // if dp[i] is prime, dp[2i], dp[3i],...,dp[ij] are all non-prime
        boolean[] dp = new boolean[n];
        int ans = 0;

        for(int i=2; i<n; i++){
            if(!dp[i]){
                ans++;
                for(int j=2; i*j<n; j++){
                    dp[i*j] = true;
                }
            }
        }

        return ans;
    }
}