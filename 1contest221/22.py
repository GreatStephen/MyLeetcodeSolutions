class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        prev = None
        
        rotten_day = -1
        eaten_day = -1
        ans = 0
        for i in range(len(apples)):
            right = days[i]
            
            if right>0:
                rotten_day = max(i+right, rotten_day)
                eaten_day = min(rotten_day, max(eaten_day,i)+apples[i])
            if right>0 and prev==None:
                prev = i
            if i==rotten_day:
                ans += (i-prev)                
                prev = None
                # print(ans)
        
        if prev!=None:
            # print(eaten_day)
            ans += (eaten_day-prev)
        return ans