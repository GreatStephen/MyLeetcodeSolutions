class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {}
        d[0] = 0
        d[1] = 1
        d[6] = 9
        d[8] = 8
        d[9] = 6
        self.ans = 0
        
        
        def isCN(num):
            n,cn = num, 0
            while n>0:
                cn = cn*10+d[n%10]
                n //= 10
            return num!=cn
        
        def helper(N, cur):
            if isCN(cur):
                self.ans += 1
            
            for n in d:
                nextn = cur*10+d[n]
                if 1<=nextn<=N:
                    helper(N, nextn)
                    
        helper(N, 0)
        return self.ans