class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[0])
        
        last_end, ans = float('-inf'), 0
        for p in pairs:
            if p[0]>last_end:
                last_end = p[1]
                ans += 1
            else:
                last_end = min(last_end, p[1])
        
        
        return ans