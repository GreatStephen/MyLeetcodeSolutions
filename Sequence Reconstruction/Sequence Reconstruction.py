class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # 超时
        indeg, d = [-1]*len(org), defaultdict(set)
        seen = set(range(1,len(org)+1))
        for adj in seqs:
            if len(adj)==1:
                if adj[0] not in range(1, len(org)+1): return False
                if indeg[adj[0]-1]<0: indeg[adj[0]-1] = 0
            else:
                for i in range(len(adj)-1):
                    # adj[i]->adj[i+1]
                    if adj[i] not in range(1, len(org)+1) or adj[i+1] not in range(1, len(org)+1):
                        return False
                    if adj[i+1] not in d[adj[i]]:
                        d[adj[i]].add(adj[i+1])
                        if indeg[adj[i]-1]<0: indeg[adj[i]-1] = 0
                        indeg[adj[i+1]-1] = 1 if indeg[adj[i+1]-1]<0 else indeg[adj[i+1]-1]+1
        # print(indeg, d)
        
        pointer = 0
        while pointer<len(org):
            zero_node = []
            for i,n in enumerate(indeg):
                if n==0: 
                    zero_node.append(i+1)
                    indeg[i] = -1
            if len(zero_node)!=1: return False
            if zero_node[0] != org[pointer]: return False
            pointer += 1
            seen.remove(zero_node[0])
            
            next_nodes = d[zero_node[0]]
            for nn in next_nodes:
                indeg[nn-1] -= 1
        
        if pointer!=len(org) or len(seen): return False
        return True