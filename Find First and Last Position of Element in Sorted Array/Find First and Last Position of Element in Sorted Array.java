// exceed 100% time and 100% space

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int lo=0;
        int hi=nums.length-1;
        int pos=-1;
        //binary search
        while(lo<=hi){
            int mid = (lo+hi)/2;
            if(nums[mid]==target){
                pos=mid;
                break;
            }
            else if(nums[mid] > target){
                hi=mid-1;
            }
            else{
                lo=mid+1;
            }
        }

        if(pos==-1){
            return new int[]{-1,-1};
        } 

        // expand from the center
        int[] res = new int[]{pos,pos};
        while(res[0]-1 >= 0){
            if(nums[res[0]-1]==target) res[0]-=1;
            else break;
        }
        while(res[1]+1 < nums.length){
            if(nums[res[1]+1]==target) res[1]+=1;
            else break;
        }

        return res;
    }
}