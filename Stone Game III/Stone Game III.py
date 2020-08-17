class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        dp = [0]*len(stoneValue)
        
        # DP. dp[i]记录Alice可以比Bob多多少分。三种情况取最大，Alice拿1/2/3个数
        # 然后Alice拿的总和减去后一个数的dp[i+1/2/3]
        # 从后往前，反推到[0]时，如果数字为正，说明Alice可以赢过Bob，反之则输

        for i in range(len(stoneValue)-1, -1, -1):
            ans, num = float('-inf'), 0
            num += stoneValue[i]
            ans = max(ans, num-(dp[i+1] if i+1<len(stoneValue) else 0))            
            if i+1<len(stoneValue):
                num += stoneValue[i+1]
                ans = max(ans, num-(dp[i+2] if i+2<len(stoneValue) else 0))
                dp[i] = ans
            if i+2<len(stoneValue):
                num += stoneValue[i+2]
                ans = max(ans, num-(dp[i+3] if i+3<len(stoneValue) else 0))
                dp[i] = ans
            dp[i] = ans
            
        if dp[0]>0: return 'Alice'
        elif dp[0]<0: return 'Bob'
        else: return 'Tie'