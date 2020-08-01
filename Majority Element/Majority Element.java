class Solution {
    public int majorityElement(int[] nums) {
        // Boyer-Moore Voting algorithm, very smart
        int res = -1;
        int count = 0;
        for(int i=0; i<nums.length; i++){
            if(count==0){
                // discard the prefix before i
                // update current res
                res = nums[i];
            }
            if(res==nums[i]){
                count++;
            }
            else{
                count--;
            }
        }

        return res;
    }
}