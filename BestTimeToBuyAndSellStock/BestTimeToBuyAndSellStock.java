class Solution {
    public int maxProfit(int[] prices) {
        int curindex=0;
        int maxindex=0;
        int MAX=0;
        while(curindex<prices.length-1){
            if(prices[curindex+1] < prices[curindex]){
                curindex++;
                continue;
            }
            maxindex=curindex;
            if(curindex>=maxindex){
                for(int j=curindex+1; j<prices.length; j++){
                    if(prices[j]>prices[maxindex]) maxindex=j;
                }
            }
            
            MAX = Math.max(MAX, prices[maxindex]-prices[curindex]);
            curindex++;
        }
        return MAX;
        
    }
}