class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # 用(idx, m)去检索(Alice score, Bob score)
        d = {} # memo
        def DP(idx, m):
            if idx>=len(piles):
                return (0,0)
            if (idx,m) in d:
                return d[(idx,m)]
            s, ans, oppo = 0, 0, 0
            for i in range(idx, idx+2*m):
                if i>=len(piles):
                    break
                s += piles[i]
                dp_ans = DP(i+1, max(m, i-idx+1)) # 计算新的idx和m，然后取memo结果
                if s+dp_ans[1]>ans: # 取当前sum+后面Alice最大值的 max
                    ans = s+dp_ans[1] # 取回来的数据，[0]代表Bob的最优解，[1]代表Alice的最优解
                    oppo = dp_ans[0]
            d[(idx,m)] = (ans, oppo) # 存储中间结果
            return (ans, oppo)
        
        ans = DP(0, 1)
        return ans[0]