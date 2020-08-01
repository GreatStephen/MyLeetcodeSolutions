class Solution {
    public void rotate(int[] nums, int k) {
        // 3 rotation solution, smart
        k %= nums.length; // if k>nums.length, make k%=length
        int left = 0, right = nums.length-1;
        reverse(nums, left, right);

        left = 0;
        right = k-1;
        reverse(nums, left, right);

        left = k;
        right = nums.length-1;
        reverse(nums, left, right);
    }

    private void reverse(int[] nums, int left, int right){
        while(left<=right){
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}