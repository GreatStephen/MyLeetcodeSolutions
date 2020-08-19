class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        
        d = {}
        def DP(N, cur): # remaining N, current number
            if (N, cur) in d:
                return d[(N, cur)]
            if N==1:
                d[(N, cur)] = [str(cur)]
                return d[(N, cur)]
            ans = []
            if cur+K<10:
                nextstr = DP(N-1, cur+K)
                for s in nextstr:
                    ans.append(str(cur)+s)
            if cur-K>=0 and cur-K!=cur+K:
                nextstr = DP(N-1, cur-K)
                for s in nextstr:
                    ans.append(str(cur)+s)
            d[(N, cur)] = ans
            return ans
        
        ans = []
        for cur in xrange(1, 10):
            temp = DP(N, cur)
            temp = map(lambda x: int(x), temp)
            if temp: 
                for t in temp:
                    ans.append(t)
        if N==1:
            ans.append(0)
        
        return ans