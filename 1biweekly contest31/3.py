class Solution:
    def numSplits(self, s: str) -> int:
        dl,dr = defaultdict(int), defaultdict(int)
        for char in s:
            dr[char]+=1
        # print(dl, dr)
        
        ans = 0
        for i in range(len(s)-1):
            dl[s[i]]+=1
            dr[s[i]]-=1
            if dr[s[i]]==0: del dr[s[i]]
            if len(dl)==len(dr): ans += 1
        
        
        return ans