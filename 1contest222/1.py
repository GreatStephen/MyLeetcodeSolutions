class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        for boxes, units in boxTypes:
            for i in range(boxes):
                heapq.heappush(heap, units)
                if len(heap)>truckSize:
                    heapq.heappop(heap)
        ans = sum(heap)
        return ans