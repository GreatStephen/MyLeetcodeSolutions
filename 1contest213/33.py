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
        for i in range(len(diff)):
            arr.insert(bisect.bisect(arr, diff[i]), diff[i])
            s = 0
            for j in range(len(arr)):
                s += arr[j]
                if s>bricks:
                    if len(arr)-j>ladders:
                        return end[i]-1
        return len(heights)-1
            