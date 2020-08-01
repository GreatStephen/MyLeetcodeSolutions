class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int ans = nums[0]+nums[1]+nums[2];
        Arrays.sort(nums);
        for(int i=0; i<nums.length-2; i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            int l = i+1, r = nums.length-1;
            while(l<r){
                int sum = nums[i]+nums[l]+nums[r];
                if(Math.abs(target-sum)<Math.abs(target-ans)) ans=sum;
                if(sum<target){
                    while(l<r&&nums[l]==nums[l+1]) l++;
                    l++;
                }
                else if(sum>target){
                    while(l<r&&nums[r]==nums[r-1]) r--;
                    r--;
                }
                else return ans;
            }
        }
        return ans;
    }
}