class Solution:
    def checkPartitioning(self, s: str) -> bool:
        palin = [[False]*len(s) for _ in range(len(s))]
        
        def checkPalin(idx):
            if idx&1:
                l,r = (idx-1)//2, (idx-1)//2+1                
            else:
                l,r = idx//2, idx//2
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                palin[l][r] = True
                l -= 1
                r += 1               
        
        for i in range(len(s)*2-1):
            checkPalin(i)
        # print(palin)
        
        dp = [[False]*len(s) for _ in range(4)]
        # dp[0][0] = True
        for k in range(1,4):
            for r in range(len(s)):
                for l in range(k-1, r+1):
                    if palin[l][r] and (l==0 or dp[k-1][l-1]):
                        dp[k][r] = True
                        break
        print(dp)
        return dp[3][-1]