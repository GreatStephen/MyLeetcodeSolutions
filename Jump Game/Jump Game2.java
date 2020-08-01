// build the dp[] from the end to the beginning
class Solution{
    public boolean canJump(int[] nums){
        if(nums.length==1) return true;
        boolean[] dp = new boolean[nums.length];
        dp[dp.length-1]=true;
        for(int i=nums.length-2; i>=0; i--){
            int steps = nums[i];
            dp[i]=false;
            for(int j=1; j<=steps; j++){
                if(i+j>=nums.length) break;
                if(dp[i+j]) dp[i]=true;
            }
        }
        return dp[0];
    }
}