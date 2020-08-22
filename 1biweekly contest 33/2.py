class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        l = [0]*n
        
        for e in edges:
            l[e[1]] += 1
        
        # print l
        ans = []
        for i,a in enumerate(l):
            if a==0:
                ans.append(i)
        
        return ans