class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])
        sorted_cost = []
        for c in cost:
            temp = []
            for i,n in enumerate(c):
                temp.append((n,i))
            temp.sort()
            sorted_cost.append(temp)
        # print(sorted_cost)
        
        g1, g2 = [0]*size1, [0]*size2
        
        def DFS(r, cur_cost):
            if r>=size1:
                if all(n==1 for n in g2): return cur_cost
                else: return None
            for cost, idx in sorted_cost[r]:
                g1[r]=1
                g2[idx]=1
                ans = DFS(r+1, cur_cost+cost)
                if ans!=None: return ans
                g2[idx]=0
            return 0
        
        
        
        
        # for c in range(size2):
        #     ans = DFS(0,c)
        #     if ans: return ans
        ans = DFS(0, 0)
        if ans!=None: return ans
        return 0