class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        cum = []
        for c in candiesCount:
            if not cum:
                cum.append(c)
            else:
                cum.append(cum[-1]+c)
        # print(cum)
        
        for favtype, favday, daycap in queries:
            most = bisect.bisect_left(cum, (favday+1)*daycap)
            # most = min(most, len(candiesCount)-1)
            least = bisect.bisect_left(cum, (favday+1))
            # print(least, most)
            
            if least<=favtype<=most:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans