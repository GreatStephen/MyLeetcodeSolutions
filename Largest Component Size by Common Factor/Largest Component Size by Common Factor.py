class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # 超时，原因在于用commonFac计算两个数字的最大公因数效率太低。union find做法是没问题的
        edges = []
        def commonFac(x,y):
            if x==y: return x
            if x>y: return commonFac(x-y, y)
            else: return commonFac(x, y-x)
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if commonFac(A[i], A[j])>1:
                    edges.append([A[i], A[j]])
        
        # print(edges)
        
        # union find
        d = {}
        for node in A:
            d[node] = node
        def findGroup(x):
            cur = x
            while cur!=d[cur]:
                cur = d[cur]
            return cur
        
        for edge in edges:
            g1, g2 = findGroup(edge[0]), findGroup(edge[1])
            if g1!=g2:
                d[g1] = g2
            d[edge[0]] = g2
            d[edge[1]] = g2
                
        
        for node in d:
            d[node] = findGroup(node)
        # print(d)
        
        ans = {}
        for node in d:
            if d[node] not in ans:
                ans[d[node]] = 0
            ans[d[node]] += 1
        return max(ans.values())
            