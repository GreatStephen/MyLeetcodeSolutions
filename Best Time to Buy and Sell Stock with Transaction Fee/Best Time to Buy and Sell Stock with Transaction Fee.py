class Solution(object):
    def maxProfit(self, prices, fee):
        # 这题跟无限次买卖完全一样。
        # buy记录买进当前price的最大值，sell记录卖出当前price的最大值。唯一的区别是卖的时候减去手续费
        # buy是用当前的钱减去price，我们追求的是最小的买进值，所以buy也取max。sell自然取max
        
        buy, sell = -prices[0], 0
        
        for i in range(1, len(prices)):
            temp = buy
            buy = max(buy, sell-prices[i])
            sell = max(sell, temp+prices[i]-fee)
        
        return sell
        