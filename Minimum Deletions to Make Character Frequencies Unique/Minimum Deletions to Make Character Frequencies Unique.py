class Solution:
    def minDeletions(self, s: str) -> int:
        ct = Counter(s)
        used = set()
        ans = 0
        for c,freq in ct.items():
            while freq>0 and freq in used:
                freq -= 1
                ans += 1
            if freq>0:
                used.add(freq)
        
        return ans