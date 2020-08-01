class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        #用堆的方法超时
        h = [(0, startFuel, -1)]
        heapq.heapify(h)
        last = target-(stations[-1][0] if stations else 0)
        
        while h:
            times, fuel, idx = heapq.heappop(h)
            idx += 1
            # print(times, fuel, idx)
            if idx>=len(stations):
                # pass the last station
                if fuel>=last: return times
                else: continue
            
            curfuel = fuel-(stations[idx][0]-(stations[idx-1][0] if idx>0 else 0))            
            # not fill
            if curfuel>=0: heapq.heappush(h, (times, curfuel, idx))
            else: continue
            # fill
            heapq.heappush(h, (times+1, curfuel+stations[idx][1], idx))
        return -1