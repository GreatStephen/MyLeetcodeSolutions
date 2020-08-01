class Solution {
    public int jump(int[] nums) {
        // DP solution, not very fast
        int length = nums.length;
        int dp[] = new int[length];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for(int i=0; i<length; i++){
            int reach = nums[i];
            int new_steps = dp[i]+1;
            
            for(int j=1; j<=reach; j++){
                if(i+j<length){
                    dp[i+j] = Math.min(dp[i+j], new_steps);
                }
                else{
                    break;
                }
            }
        }

        return dp[length-1];
    }
}