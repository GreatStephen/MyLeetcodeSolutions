class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = [1]*21
        for i in range(2,20):
            length[i] = length[i-1]*2+1
        # print(length)
        
        def helper(n,k,r):
            # print(n,k,r)
            # l = length[n]
            if n==1: return '1' if r else '0'
            c = None
            if k<=length[n-1]:
                c = helper(n-1, k, False)
            
            elif k==(length[n-1]+1):
                return '1' if not r else '0'
            
            else:
                pos = length[n]-k+1
                # print(n,k,r,pos)
                c = helper(n-1, pos, True)
                
            if r:
                return '1' if c=='0' else '0'
            else:
                return c
        
        return helper(n,k,False)