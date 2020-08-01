class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # dijkstra算法，heap按元组的第一个排序，从小到大，以后可以利用这个特点
        # 这个方法不更新heap的最短距离，而是另开一个最短距离放进heap
        # 非最优解被取出来之后，再往里放的东西也是非最优的，相当于无效
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)] # (price, current node, stops left)
        while heap:
            # 取出来的可能是非最优解
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    # 如果取出非最优解，再push进去的也是非最优解
                    # 如果k<=0，就不会再放进新的元素了
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1 