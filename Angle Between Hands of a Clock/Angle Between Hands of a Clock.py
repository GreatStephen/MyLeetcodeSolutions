class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = 6*(minutes - (hour if hour<12 else 0)*5)
        ans -= 30*(minutes/60)
        return min(abs(ans), 360-abs(ans))