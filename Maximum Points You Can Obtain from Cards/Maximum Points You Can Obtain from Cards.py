class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # fixed-size window，很简单
        total = sum(cardPoints)
        s, r, ans = 0, 0, 0
        while r < (len(cardPoints)-k):
            s += cardPoints[r]
            r += 1
        l, r = 0, r-1
        while r<len(cardPoints):
            ans = max(ans, total-s)
            r += 1
            if r>=len(cardPoints): break
            s += cardPoints[r]
            s -= cardPoints[l]
            l += 1
            
        return ans