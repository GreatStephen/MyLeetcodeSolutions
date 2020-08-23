class Solution(object):
    def mostVisited(self, n, rounds):
        ans = []
        idx = 0
        start = rounds[0]
        init = rounds[0]
        
        while idx<len(rounds):
            
            if start == init:
                ans = []
            ans.append(start)    
            if start==rounds[idx]:
                idx += 1
            start = (start+1)%(n+1)
            if not start: start+=1
        
        ans.sort()
        return ans
            