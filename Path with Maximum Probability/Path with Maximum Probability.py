class Solution:
    h_dict = collections.defaultdict(float)

    class Item():
        def __init__(self, e1, e2):
            self.e = (e1, e2)
            self.out = Solution()
        def __lt__(self, other):
            if self.out.h_dict[self.e]>self.out.h_dict[other.e]: return True
            else: return False
        def __str__(self):
            return str(self.e)
        def __repr__(self):
            return str(self.e)

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edge_dict = collections.defaultdict(float)
        adj_dict = collections.defaultdict(list)
        for e,p in zip(edges, succProb):
            edge_dict[(e[0], e[1])] = p
            edge_dict[(e[1], e[0])] = p
            adj_dict[e[0]].append(e[1])
            adj_dict[e[1]].append(e[0])
        # print(edge_dict)

        h = []
        heapq.heapify(h)
        seen = collections.defaultdict(float)
        for node in adj_dict[start]:
            item = self.Item(start, node)
            self.h_dict[item.e] = edge_dict[item.e]
            heapq.heappush(h,item)
        seen[start] = 1
        # print(h[0])

        while len(h)>0:
            item = heapq.heappop(h)
            if item.e[1] in seen: continue
            seen[item.e[1]] = seen[item.e[0]] * edge_dict[item.e]
            if item.e[1]==end: return seen[item.e[1]]   # find the result
            for node in adj_dict[item.e[1]]:
                if node not in seen:
                    next_item = self.Item(item.e[1], node)
                    self.h_dict[next_item.e] = edge_dict[next_item.e] * seen[item.e[1]]
                    heapq.heappush(h, next_item)   

        return 0.0