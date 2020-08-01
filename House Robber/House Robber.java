class Solution {
    /* Memoization
    int[] memo;
    
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        memo = new int[nums.length];
        Arrays.fill(memo, -1);
        int sum0=0, sum1=0;
        
        sum0 = Math.max(nums[0] + recur(nums, 2), sum0);
        sum0 = Math.max(nums[0] + recur(nums, 3), sum0);
        sum1 = Math.max(nums[1] + recur(nums, 3), sum1);
        sum1 = Math.max(nums[1] + recur(nums, 4), sum1);
        return Math.max(sum0, sum1);
    }
    
    public int recur(int[] nums, int index ){
        if(index>=nums.length) return 0;
        if(memo[index] >= 0) return memo[index];
        if(index==nums.length-1){
            memo[index]=nums[index];
            return nums[index];
        }
        else if(index==nums.length-2){
            memo[index]=Math.max(nums[index], nums[index+1]);
            return Math.max(nums[index], nums[index+1]);
        }
        
        int res1 = nums[index] + recur(nums, index+2);
        memo[index] = res1;
        int res2 = nums[index+1] + recur(nums, index+3);
        memo[index+1] = res2;
        return Math.max(res1, res2);
    }
    */
    
    public int rob(int[] nums) {
        if(nums.length==0) return 0;
        if(nums.length==1) return nums[0];
        if(nums.length==2) return Math.max(nums[0], nums[1]);
        int[] res = new int[nums.length];
        int index=nums.length-1;
        for(; index>=0; index--){
            if(index==nums.length-1 || index==nums.length-2) res[index]=nums[index];
            else if(index==nums.length-3) res[index] = nums[index]+nums[index+2];
            else res[index] = nums[index]+Math.max(res[index+2], res[index+3]);
        }
        
        return Math.max(res[0], res[1]);
    }
}