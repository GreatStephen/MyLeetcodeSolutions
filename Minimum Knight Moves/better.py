class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # 这个厉害了，因为四个方向是对称的，所以人为把坐标限定在第一象限
        # 然后两个方向取最小值。用lru cache做memo
        @lru_cache(None)
        def dp(x,y):
            if x+y==0: return 0
            if x+y==1: return 3
            if x+y==2: return 2
            return min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1)))+1
        
        return dp(abs(x), abs(y))
        