class Solution {
    public boolean canPartition(int[] nums) {
        // DP solution very smart
        // O(N*sum)
        int sum=0;
        for(int i=0; i<nums.length; i++){
            sum += nums[i];
        }

        if(sum%2==1){
            return false;
        }

        sum /=2;

        boolean[] dp = new boolean[sum+1];
        dp[0] = true;

        for(int i=1; i<dp.length; i++){
            dp[i] = false;
        }

        for(int i=1; i<=nums.length; i++){
            for(int j=dp.length-1; j>=0; j--){
                // no need for nums[i-1]? dp[j] = dp[j]
                // need nums[i-1]? dp[j] = dp[j-nums[i-1]], that's why traverse from tail to head
                dp[j] = dp[j] || (j-nums[i-1]>=0?dp[j-nums[i-1]]:false);
            }
        }

        return dp[sum];

    }
}