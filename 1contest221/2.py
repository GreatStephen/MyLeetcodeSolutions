class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        val = [0]*40000
        
        for i in range(len(apples)):
            val[i] += apples[i]
            val[i+min(days[i], apples[i])] -= apples[i]
            # print(val)
        
        cum = []
        for v in val:
            if not cum:
                cum.append(v)
            else:
                cum.append(v+cum[-1])
        # print(cum)
        
        ans = 0
        for v in cum:
            if v>0:
                ans += 1
        return ans