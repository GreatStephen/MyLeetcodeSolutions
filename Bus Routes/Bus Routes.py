class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        d = {}
        for i,route in enumerate(routes):
            for r in route:
                if r not in d: d[r] = set()
                d[r].add(i)
        
        seen = set()
        deq = deque()
        deq.append((S, 0))
        while deq:
            curstop, count = deq.popleft()
            if curstop==T: return count
            seen.add(curstop)
            buses = d[curstop]
            for b in buses:
                for st in routes[b]:
                    if st not in seen:
                        deq.append((st, count+1))
                        # if st==T: return count+1
                routes[b] = [] # 很关键，把这辆车的信息抹去，减少很多时间，否则TLW
        
        return -1
            