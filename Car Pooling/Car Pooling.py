class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # 按站点位置sort。再按上客、下客数量从小到大排序，因为先下人后上人
        arr = []
        for t in trips:
            arr.append([t[1], t[0]])
            arr.append([t[2], -t[0]])
        arr.sort()
        
        cur = 0
        for a in arr:
            cur += a[1]
            if cur<0 or cur>capacity: return False
        return True