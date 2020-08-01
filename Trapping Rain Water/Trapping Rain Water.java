class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right =  height.length-1;
        int maxleft = 0;
        int maxright = 0;
        int res=0;
        
        while(left<right){
            int height_left = height[left];
            int height_right = height[right];
            if(height_left < height_right){
                if(height_left>=maxleft){
                    maxleft = height_left;
                    left++;
                }
                else{
                    res += maxleft - height_left;
                    left++;
                }
            }
            else{
                if(height_right>=maxright){
                    maxright = height_right;
                    right--;
                }
                else{
                    res += maxright - height_right;
                    right--;
                }
            }
        }
        
        return res;
    }
}