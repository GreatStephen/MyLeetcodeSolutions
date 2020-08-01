class Solution {
    public int maxProfit(int[] prices) {
        // 1-pass traversal
        int cur_lo = -1;
        int cur_hi = -1;
        int ans = 0;

        for(int i=2; i<prices.length; i++){
            if(prices[i]>prices[i-1]){
                // going up
                if(cur_lo==-1) cur_lo=prices[i-1];
                cur_hi = prices[i];
            }
            else if(prices[i]<prices[i-1]){
                // going down
                if(cur_hi!=-1){
                    ans += cur_hi-cur_lo;
                    cur_hi=-1;
                    cur_lo=-1;
                }
            }
        }
        if(cur_hi!=-1 && cur_lo!=-1){
            ans += cur_hi-cur_lo;
        }

        return ans;
    }
}