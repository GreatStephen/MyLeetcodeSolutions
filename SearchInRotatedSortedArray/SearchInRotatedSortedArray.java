class Solution {
    public int search(int[] nums, int target) {
        // find the pivot by traversing the array
        int pivot=0;
        while(pivot<nums.length-1 && nums[pivot]<nums[pivot+1]){
            pivot++;
        }
        pivot++;
        
        // reconstruct the array
        int[] new_nums;
        if(pivot==nums.length) new_nums = nums;
        else{
            new_nums = new int[nums.length];
            int temp_index = pivot;
            for(int i=0; i<nums.length; i++){
                new_nums[i] = nums[temp_index];
                temp_index++;
                if(temp_index>=nums.length) temp_index=0;
            }
        }
        
        // binary search
        int lo=0, hi=nums.length-1;
        int mid = (lo + hi)/2;
        int res=-1;
        while(lo <= hi){
            if(new_nums[mid]==target){
                res = mid;
                break;
            }
            else if(new_nums[mid]<target){
                lo = mid+1;
                mid = (lo + hi)/2;
            }
            else{
                hi = mid-1;
                mid = (lo + hi)/2;
            }
        }
        
        // find the original index in nums[]
        if(res<0) return -1;
        else return (res<(nums.length-pivot))?res+pivot : res+pivot-nums.length;
    }
}