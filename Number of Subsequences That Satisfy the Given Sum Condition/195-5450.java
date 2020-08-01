class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length-1;
        int ans = 0;
        while(nums[left]*2<=target){
            if(nums[left]+nums[right]>target){
                right--;
                
                // continue;
            }
            else{
                int num_between = Math.max(0, right-left-1);
                // if(nums[left]==8) System.out.println(ans);
                double addition = Math.pow(2, num_between);
                addition %=(Math.pow(10,9)+7);
                ans+=addition;
                ans %= (Math.pow(10,9)+7);
                right--;
            }
            if(left>right){
                right = nums.length-1;
                left++;
            }
            if(left>=nums.length) break;
        }

        
        return ans;
    }
}



class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int left = 0, right = nums.length-1;
        int ans = 0;
        int MOD = (int)1e9+7;
        int[] pows = new int[nums.length];
        pows[0] = 1;
        for(int i=1; i<pows.length; i++)
            pows[i] = pows[i-1]*2 %MOD;
        while(left<=right){
            if(nums[left]+nums[right]<=target){
                ans += pows[right-left++];
                ans %= MOD;
            }
            else{
                right--;
            }
        }
        return ans;
    }
}