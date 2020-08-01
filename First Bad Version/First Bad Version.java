/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

      public class Solution extends VersionControl {
        public int firstBadVersion(int n) {
            // Binary Search
            // (lo+hi)/2 will cause integer overflow
            // must use lo+(hi-lo)/2
            int lo = 1;
            int hi = n;
            int mid = lo+(hi-lo)/2;

            while(hi>lo){
                if(isBadVersion(mid)){
                    hi = mid;
                    mid = lo+(hi-lo)/2;
                }
                else{
                    lo = mid+1;
                    mid = lo+(hi-lo)/2;
                }
            }

            return lo;
        }
    }