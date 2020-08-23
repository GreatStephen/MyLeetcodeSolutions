class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        ans = 0
        while piles:
            ans += piles[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
        return ans