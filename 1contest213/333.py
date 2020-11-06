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
        
        arr = []
        sum_br = 0
        num_la = ladders
        for i in range(len(diff)):
            if sum_br+diff[i]<=bricks:
                arr.insert(bisect.bisect(arr,diff[i]), diff[i])
                sum_br += diff[i]
            elif arr and diff[i]<arr[-1]:
                sum_br += diff[i]-arr[-1]
                num_la -= 1
                arr.pop()
                arr.insert(bisect.bisect(arr,diff[i]), diff[i])
            else:
                num_la-=1
            # print(sum_br, num_la)
            if num_la<0:
                return end[i]-1
        return len(heights)-1
            