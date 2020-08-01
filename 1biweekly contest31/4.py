class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not len(target): return 0
        subs = []
        l, r = -1,-1
        MIN = min(target)
        for i in range(len(target)):
            target[i]-=MIN
            if target[i]>0:
                if l==-1: l = r = i
                else: r = i
            else:
                if l!=-1 and r!=-1: 
                    subs.append(target[l:r+1])
                    l = r = -1
        if l!=-1 and r!=-1: 
            subs.append(target[l:r+1])
        
        # print(subs)
        ans = MIN
        for sub in subs:
            ans += self.minNumberOperations(sub)        
        
        return ans