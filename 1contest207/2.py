class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        
        def DFS(start, seen):
            if start==len(s):
                return 0
            temp = ''
            ans = -1
            for i in range(start, len(s)):
                temp += s[i]
                if temp in seen: continue
                seen.add(temp)
                next_ans = DFS(i+1, seen)
                # ans = max(ans, 1+DFS(i+1, seen))
                if next_ans!=-1: ans = max(ans, 1+next_ans)
                seen.remove(temp)
            return ans
        
        
        ans = max(ans, DFS(0, set()))
        return ans