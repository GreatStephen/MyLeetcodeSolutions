class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if k>0:
            s, idx = sum(code[1:k+1]), (k+1)%len(code)

            for i in range(len(code)):
                ans.append(s)
                s -= (code[i+1] if i+1<len(code) else 0)
                s += code[idx]
                idx = (idx+1)%len(code)
                
        elif k==0:
            ans = [0]*len(code)
        else:
            s, idx = sum(code[len(code)+k:len(code)]), len(code)+k

            for i in range(len(code)):
                ans.append(s)
                s -= code[idx]
                idx = (idx+1)%len(code)
                s += code[i]
                        
        return ans