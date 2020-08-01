//i是慢指针，j是快指针
class Solution {
    public int removeDuplicates(int[] nums) {
        int i=0,j=0;
        for(j=0;j<nums.length;j++){
            if(nums[i]==nums[j]) continue;
            else nums[++i]=nums[j];
        }
        return i+1;
    }
}