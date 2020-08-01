class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None]*len(s)
        for i,ind in enumerate(indices):
            ans[ind] = s[i]
        print(str(ans))
        
        a = ''
        for c in ans: a+=c
        
        return a