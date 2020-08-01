class Solution {
    public int missingNumber(int[] nums) {
        int[] judge = new int[nums.length+1];
        Arrays.fill(judge, 1);

        for(int num: nums){
            if(judge[num]>0){
                judge[num] *= -1;
            }
        }

        for(int i=0; i<judge.length; i++){
            if(judge[i]>0) return i;
        }

        return -1;
    }
}