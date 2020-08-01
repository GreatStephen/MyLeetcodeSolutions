class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 拓扑，每次减去leaf，速度慢，需要遍历dict
        d = collections.defaultdict(set)
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        nodes = {i for i in range(n)}
        while len(nodes)>2:
            leaf_set = {i for i in d if len(d[i])==1}
            nodes -= leaf_set
            for leaf in leaf_set:
                for n in d[leaf]: d[n].remove(leaf)
                del d[leaf]
        return list(nodes)  
