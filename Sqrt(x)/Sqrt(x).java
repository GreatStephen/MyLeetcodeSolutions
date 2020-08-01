class Solution {
    public int mySqrt(int x) {
        // binary search
        if(x<2) return x;
        int left = 0;
        int right = x/2;
        int mid = left+(right-left)/2;
        int ans = -1;

        while(left<=right){
            long temp = (long)mid*mid;
            if(temp==x) return mid;
            else if(temp<x){
                ans = Math.max(ans, mid);
                left = mid+1;
                mid = left+(right-left)/2;
            }
            else{
                right = mid-1;
                mid = left+(right-left)/2;
            }
        }
        
        return ans;
    }
}