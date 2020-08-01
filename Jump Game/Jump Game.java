
// Time limit exceeded

class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length==0) return false;
        if(nums.length==1) return true;
        int counter=1;
        boolean res = false;
        for(int i=nums.length-2; i>=0; i--){
            // System.out.println(counter);
            if(counter <= nums[i]){
                // System.out.println(nums[i]);
                res = dfs(nums, i);
                if(res) return res;
            } 
            counter++;
        }

        return false;
    }

    public boolean dfs(int[] nums, int index){
        if(index==0) return true;
        int counter=1;
        boolean res=false;
        for(int i=index-1; i>=0; i--){
            if(counter <= nums[i]){
                res = dfs(nums, i);
                if(res) return res;
            } 
            counter++;
        }
        return false;
    }
}