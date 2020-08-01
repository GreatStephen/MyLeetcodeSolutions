class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int a : nums) {
            res = res ^ a;
        }
        return res;
    }
}