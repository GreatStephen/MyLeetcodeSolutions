class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = {}
        ans = None
        Max = 0
        for i in range(len(keysPressed)):
            c = keysPressed[i]
            # if c not in time:
            #     time[c] = 0
            t = releaseTimes[i]- (releaseTimes[i-1] if i>0 else 0)
            if t>Max:
                ans = c
            elif t==Max:
                ans = max(ans, c)
            Max = max(Max, t)
        
#         ans = None
#         Max = 0
#         for k in time.keys():
#             if time[k]>Max:
#                 ans = k
#             elif time[k]==Max:
#                 ans = max(ans, k)
#             Max = max(time[k], Max)
        
        # print(time)
        return ans