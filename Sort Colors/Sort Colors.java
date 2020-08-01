class Solution {
    public void sortColors(int[] nums) {
        int cur=0;
        int p0=0;
        int p2=nums.length-1;
        while(p0<nums.length && nums[p0]==0) p0++;
        while(p2>=0 && nums[p2]==2) p2--;
        if(cur<p0) cur=p0;

        while(cur<=p2){
            if(nums[cur]==0){
                nums[cur]=nums[p0];
                nums[p0]=0;
                while(nums[p0]==0) p0++;
                if(cur<p0) cur=p0;
                // else cur++;
            }
            else if(nums[cur]==2){
                nums[cur]=nums[p2];
                nums[p2]=2;
                while(nums[p2]==2) p2--;
                if(cur==p0){
                    while(nums[p0]==0) p0++;
                    if(cur<p0) cur=p0;
                }
            }
            else cur++;
        }
    }
}