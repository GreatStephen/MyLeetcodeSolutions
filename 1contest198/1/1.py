class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        n = numBottles
        full, emp = numBottles, 0
        while full>0:
            # print(full, emp)
            ans += full
            
            emp += full
            full = 0
            full = emp//numExchange
            emp %= numExchange
            
        return ans