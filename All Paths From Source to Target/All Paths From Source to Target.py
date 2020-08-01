class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []
        def DFS(node, path):
            path.append(node)
            if node==N-1: 
                ans.append(path[:])
                return
            for n in graph[node]:
                DFS(n, path[:])

        DFS(0,[])
        return ans