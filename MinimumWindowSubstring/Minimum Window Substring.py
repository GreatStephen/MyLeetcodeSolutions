class Solution:
    def minWindow(self, S: str, T: str) -> str:
        need = Counter(T)
        # print(need)
        missing = len(T)
        ansi, ansj =-1,-1
        i = 0
        for j,c in enumerate(S, 1):
            if need[c]>0:
                missing -= 1
            need[c] -= 1
            # print(need, missing)
            if not missing:
                while i<j and need[S[i]]<0:
                    need[S[i]] += 1
                    i += 1
                if ansj<0 or j-i<ansj-ansi:
                    ansi, ansj = i, j
        
        
        return S[ansi:ansj]