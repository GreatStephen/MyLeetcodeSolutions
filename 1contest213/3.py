class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff, end = [], []
        for i in range(1, len(heights)):
            if heights[i]>heights[i-1]:
                diff.append(heights[i]-heights[i-1])
                end.append(i)
        
        if not diff:
            return len(heights)-1
        # print(diff, end)
        
        @lru_cache(None)
        def DP(index, br, la):
            if index==len(diff):
                return len(heights)-1
            if la==0 and br<diff[index]: 
                # print(index)
                return end[index]-1
            
            ans = 0
            if la>0:
                ans = max(ans, DP(index+1, br, la-1))
            if br>=diff[index]:
                ans = max(ans, DP(index+1, br-diff[index], la))
            return ans
        
        return DP(0, bricks, ladders)