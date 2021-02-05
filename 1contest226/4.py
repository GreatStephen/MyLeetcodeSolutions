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
        
        def DFS(cur, k):
            if k==0:
                if cur==len(s):
                    return True
                else:
                    return False
            for j in range(cur, len(s)):
                if palin[cur][j]:
                    if DFS(j+1, k-1):
                        return True
            return False
            
            
        return DFS(0, 3)