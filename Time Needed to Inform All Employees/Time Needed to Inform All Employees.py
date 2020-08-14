class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        
        self.ans = 0
        adj = [None]*n
        for i,h in enumerate(manager):
            if h==-1:
                continue
            if adj[h]==None:
                adj[h] = set()
            adj[h].add(i)
        
        
        # print adj
        def DFS(node, cur):
            nexts = adj[node]
            if not nexts:
                self.ans = max(self.ans, cur)
                return
            for n in nexts:
                DFS(n, cur+informTime[node])
            
        
        
        DFS(headID, 0)
        return self.ans