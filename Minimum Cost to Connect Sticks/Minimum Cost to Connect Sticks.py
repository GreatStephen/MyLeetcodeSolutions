class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # use min-heap for this problem. Same as Huffman Tree
        heapq.heapify(sticks)
        ans = 0
        while len(sticks)>1:
            e1, e2 = heapq.heappop(sticks), heapq.heappop(sticks)
            heapq.heappush(sticks, e1+e2)
            ans+=e1+e2
        return ans