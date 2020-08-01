import java.util.Deque;

class Solution {
    public int lengthOfLIS(int[] nums) {
        if(nums.length==0) return 0;
        int res=1;
        int[] dp = new int[nums.length];
        dp[0]=1;

        for(int i=1; i<nums.length; i++){
            int max_temp=0;
            for(int j=0; j<i;j++){
                if(nums[j]<nums[i]){
                    max_temp = Math.max(max_temp, dp[j]);
                }
            }
            dp[i] = max_temp+1;
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}