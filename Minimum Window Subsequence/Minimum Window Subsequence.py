class Solution:
    def minWindow(self, S: str, T: str) -> str:
        l, r, tid = 0, 0, 0
        ansi, ansj = -1, -1
        
        # 2次匹配。先用r匹配到第一个T[-1]，然后l从r的位置往前寻找第一个T[0]。
        # 此时[l:r+1]是一个正确结果，再判断它是否minimum
        while r<len(S):
            if S[r]==T[tid]:
                tid += 1
            if tid==len(T): # 已找到T的结尾char
                tid -= 1
                l = r
                while l>=0: # l从r的位置开始往前找
                    if S[l]==T[tid]:
                        tid -= 1                        
                    if tid<0:
                        break
                    l -= 1    
                tid = 0 # 此时，l,r分别指向substring的第一个和最后一个字符
                if ansj<0 or r-l+1<ansj-ansi:
                    ansj = r+1
                    ansi = l
                r = l
            
            r += 1
        
        if ansj<0: return ''
        return S[ansi:ansj]