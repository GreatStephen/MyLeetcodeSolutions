class Solution:
    @lru_cache(maxsize=None)
    def winnerSquareGame(self, n: int) -> bool:
        if n==0: return False
        for i in range(int(math.sqrt(n)), 0, -1):
            if not self.winnerSquareGame(n-i*i): return True
        return False