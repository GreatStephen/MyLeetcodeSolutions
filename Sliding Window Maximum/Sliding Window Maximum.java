class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // DP solution, very concise and smart
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] res = new int[nums.length-k+1];

        // initial left[]
        int max=0;
        for(int i=0; i<nums.length; i++){
            // start of a block
            if(i%k==0){
                max = nums[i];
            }
            else{
                max = Math.max(max, nums[i]);
            }
            left[i] = max;
        }

        // initial right[]
        for(int i=nums.length-1; i>=0; i--){
            if(i==nums.length-1 || (i+1)%k==0){
                max = nums[i];
            }
            else{
                max = Math.max(max, nums[i]);
            }
            right[i] = max;
        }

        // traverse nums[], O(N)
        for(int i=0; i+k-1<nums.length; i++){
            int j = i+k-1;
            res[i] = Math.max(left[j], right[i]);
        }

        return res;

    }
}