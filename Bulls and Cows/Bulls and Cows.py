class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        num = [0]*10
        
        for i in range(len(secret)):
            c1, c2 = secret[i], guess[i]
            if c1==c2: 
                A += 1
                continue
            if num[int(c1)]<0: B += 1
            if num[int(c2)]>0: B += 1
            num[int(c1)] += 1
            num[int(c2)] -= 1
        
        return str(A)+'A'+str(B)+'B'