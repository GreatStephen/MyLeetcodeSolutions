class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10: return None
        d, ans = {'A':0, 'C':1, 'G':2, 'T':3}, []
        seen, dup = set(), set()
        l, r, sum = 0, 0, 0
        for r in range(9):
            sum<<=2 # sum*4
            sum+=d[s[r]]
        for r in range(9,len(s)):
            sum<<=2
            sum+=d[s[r]]
            if sum not in seen:
                seen.add(sum)
            elif sum not in dup:
                ans.append(s[l:r+1])
                dup.add(sum)
            sum %= 1<<18
            l += 1     
        return ans