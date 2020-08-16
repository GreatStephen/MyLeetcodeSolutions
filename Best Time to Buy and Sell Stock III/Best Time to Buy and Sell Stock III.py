class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 一维的dp。记录在当前price下，第一次买，第一次卖，第二次买，第二次卖，分别多少钱
        # 这四个数，买进价取最小值，卖出价取最大值
        # 当所有price遍历过去之后，剩下的price2就是两次买卖所得的最大利润
        buy1,sell1,buy2,sell2 = float('inf'),0,float('inf'),0
        for p in prices:
            buy1 = min(buy1, p)
            sell1 = max(sell1, p-buy1)
            buy2 = min(buy2, p-sell1)
            sell2 = max(sell2, p-buy2)
        return sell2