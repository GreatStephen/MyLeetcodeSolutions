// 1.slow pointing to the first zero
// 2.fast pointing to the first non-zero digit after slow
// 3.swap slow and fast
// 4.move slow to the right, move fast to the right
class Solution {
    public void moveZeroes(int[] nums) {
        int slow = 0, fast = 0;
        while (fast < nums.length) {
            // first 0
            for (slow = slow; slow < nums.length; slow++) {
                if (nums[slow] == 0) break;
            }
            if (slow == nums.length)
                return;
            if(fast<slow) fast=slow;
            // first non-0
            for (fast=fast; fast < nums.length; fast++) {
                if (nums[fast] != 0) break;
            }
            if (fast == nums.length)
                return;

            int temp=nums[slow];
            nums[slow]=nums[fast];
            nums[fast]=temp;
        }

    }
}