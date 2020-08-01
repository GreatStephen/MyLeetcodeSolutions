class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ans = new int[2];
        int left=0, right=numbers.length-1;
        while(left<right){
            if(numbers[left]+numbers[right]>target){
                while(left<right && numbers[right]==numbers[right-1]) right--;
                right--;
            }
            else if(numbers[left]+numbers[right]<target){
                while(left<right && numbers[left]==numbers[left+1]) left++;
                left++;
            }
            else{
                ans[0]=left+1;
                ans[1]=right+1;
                break;
            }
        }
        return ans;
    }
}