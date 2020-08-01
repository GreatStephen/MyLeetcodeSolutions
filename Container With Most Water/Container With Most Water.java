class Solution {
    public int maxArea(int[] height) {
        int left=0; 
        int right = height.length-1;
        int Max = 0;
        while(left<right){
            int shorter = height[left]<=height[right]?left:right;
            int area = (right-left)*height[shorter];
            Max = Math.max(Max, area);
            if(shorter==left) left++;
            else right--;
        }

        return Max;
    }
}