class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # check if every adj in org is also adj in seqs
        # 不能检测环
        d = defaultdict(int)
        if len(org)==1:
            d[0] = org[0]
        for i in range(len(org)-1):
            d[org[i]] = org[i+1]
        
        seen = set()
        for s in seqs:
            if s[0] not in range(1,len(org)+1): return False
            if len(s)==1:                
                # if 0 not in d or d[0]!=s[0]: return False
                # else: seen.add(s[0])
                if 0 in d and d[0]==s[0]: seen.add(s[0])
            else:                
                for i in range(len(s)-1): 
                    if s[i+1] not in range(1,len(org)+1): return False
                    if d[s[i]]==s[i+1]:
                        seen.add(s[i])
        # print(seen, d)
        if len(seen)!=len(d): return False
        return True