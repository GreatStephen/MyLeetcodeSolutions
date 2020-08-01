class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP question
        # use 2 dp arrays sell[] and buy[], cuz there are 2 states
        if len(prices)==0:
             return 0
        buy, sell = [], []
        buy.append(0-prices[0])
        sell.append(0)
        for i,v in enumerate(prices, 1):
            buy.append(max(buy[i-1], (sell[i-2] if i>=2 else 0)-v))
            sell.append(max(buy[i-1]+v, sell[i-1]))
        return sell[-1]