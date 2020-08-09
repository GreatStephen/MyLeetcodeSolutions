class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = [] # [[i,j]]
        cum = 0
        d = {0:[-1]}
        
        for j,n in enumerate(nums):
            cum += n
            if cum-target in d:
                l = d[cum-target]
                for i in l:
                    res.append([i+1,j])
            
            if cum not in d:
                d[cum] = []
            d[cum].append(j)
        
        # print(res)
        
        
        res = sorted(res, key=lambda x:(x[1]-x[0]))
        print(res)
        
        s, e = [], []
        for inter in res:
            # print(inter)
            if not s and not e: 
                s.append(inter[0])
                e.append(inter[1])
                continue
            else:
                pos = bisect.bisect(e, inter[0])
                if pos==0:
                    if inter[1]<s[0]:
                        s.insert(0, inter[0])
                        e.insert(0, inter[1])                
                else:
                    if e[pos-1]==inter[0]:
                        continue
                    elif pos==len(e):
                        s.append(inter[0])
                        e.append(inter[1])
                    elif s[pos]>inter[1]:
                        s.insert(pos,inter[0])
                        e.insert(pos,inter[1])
        
        # print(s, e)
        return len(s)       
                
                