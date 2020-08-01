class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 2 pointers, record the last occurence of each letter
        d, ans = {}, []
        for i,c in enumerate(S): d[c] = i
        
        idx, last, prev = 0, 0, 0
        while idx<len(S):
            last = max(last, d[S[idx]])
            if last==idx:
                ans.append(last-prev+1)
                prev = idx+1
            idx+=1
        return ans        