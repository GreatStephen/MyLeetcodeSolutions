class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find确实速度偏慢
        ntog = {} # nodes to groups
        gton = {} # groups to nodes
        
        for gid,edge in enumerate(edges):
            if edge[0] in ntog and edge[1] in ntog and ntog[edge[0]]==ntog[edge[1]]:
                continue
            gton[gid] = set()
            for node in edge:
                # gton[gid] = set()
                gton[gid].add(node)
                if node not in ntog:
                    ntog[node] = gid
                else:
                    lastgid = ntog[node]
                    for lastnode in gton[lastgid]:
                        ntog[lastnode] = gid
                        gton[gid].add(lastnode)
                    gton.pop(lastgid)
        
        return len(gton)+n-len(ntog)