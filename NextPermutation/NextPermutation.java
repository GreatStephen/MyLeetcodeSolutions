import java.util.Arrays;

class Solution {
    public void nextPermutation(int[] nums) {
        int i,j;
        int temp;
        if(nums.length<=1) return;
        for(i=nums.length-2;i>=0;i--){
            if(nums[i]<nums[i+1]) break;
        }

        if(i==-1){
            i=0;
            j=nums.length-1;
            while(i<j){
                temp = nums[i];
                nums[i]=nums[j];
                nums[j]=temp;
                i++;
                j--;
            }
            return;
        }
        for(j=nums.length-1;j>i;j--){
            if(nums[j]>nums[i]) break;
        }

        temp = nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
        i++;
        j=nums.length-1;
        while(i<j){
            temp = nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            i++;
            j--;
        }

    }
}