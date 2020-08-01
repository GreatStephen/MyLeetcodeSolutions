class Solution {
    public int[] countBits(int num) {
        // DP with last set bit
        int[] res = new int[num+1];
        res[0] = 0;
        for(int i=1; i<res.length; i++){
            res[i] = 1 + res[i&(i-1)];
        }

        return res;
    }
}