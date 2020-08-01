import java.util.Arrays;

class Solution {
    public int firstMissingPositive(int[] nums) {
        boolean present = false;
        int n = nums.length;
        int res = -1;

        // initialize
        for(int i=0; i<n; i++){
            if(nums[i]==1){
                present = true;
            }
            if(nums[i]<=0 || nums[i]>n){
                nums[i] = 1;
            }
        }
        if(!present){
            return 1;
        }

        // traverse
        for(int num: nums){
            int abs_num = Math.abs(num);
            if(abs_num==n){
                if(nums[0]>0){
                    nums[0]*=-1;
                }
            }
            else if(nums[abs_num]>0){
                nums[abs_num]*=-1;
            }
        }

        // find the result
        for(int i=1; i<n; i++){
            if(nums[i]>0){
                res = i;
                return res;
            }
        }
        if(nums[0]>0){
            return n;
        }
        return n+1;
    }
}