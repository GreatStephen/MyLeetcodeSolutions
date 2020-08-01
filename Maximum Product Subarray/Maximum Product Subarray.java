class Solution {
    public int maxProduct(int[] nums) {
        if(nums.length==0) return nums[0];
        int res=nums[0];
        int min=nums[0];
        int max=nums[0];

        for(int i=1; i<nums.length; i++){
            if(nums[i]<0){
                int temp=min;
                min=max;
                max=temp;
            }
            min = Math.min(nums[i], nums[i]*min);
            max = Math.max(nums[i], nums[i]*max);
            res = Math.max(res, max);
        }

        return res;
    }
}