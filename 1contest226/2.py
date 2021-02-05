class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = {}
        heads = set()
        for n1, n2 in adjacentPairs:
            if n1 not in edges:
                edges[n1] = set()
            if n2 not in edges:
                edges[n2] = set()
            if n1 not in heads:
                heads.add(n1)
            else:
                heads.remove(n1)
            if n2 not in heads:
                heads.add(n2)
            else:
                heads.remove(n2)    
            edges[n1].add(n2)
            edges[n2].add(n1)
        # print(list(heads))
        
        visited = set()
        ans = []
        node = list(heads)[0]
        visited.add(node)
        for i in range(len(adjacentPairs)+1):
            ans.append(node)
            for next_node in edges[node]:
                if next_node not in visited:
                    node = next_node
                    visited.add(next_node)
        return ans
            