class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # heap TLE
        h = []
        heapq.heapify(h)
        
        for i,w in enumerate(workers):
            for j,b in enumerate(bikes):
                item = (abs(w[0]-b[0])+abs(w[1]-b[1]), i, j)
                heapq.heappush(h, item)
        
        seenw, seenb = set(), set()
        ans = [0]*len(workers)
        while h:
            item = heapq.heappop(h)
            if item[1] not in seenw and item[2] not in seenb:
                ans[item[1]] = item[2]
                seenw.add(item[1])
                seenb.add(item[2])
        return ans