class Solution:
    def wordsAbbreviation(self, D: List[str]) -> List[str]:
        def Abbr(s, k):
            if k>=len(s)-2: return s
            ans = s[:k] + str(len(s)-k-1) + s[-1]
            return ans
        
        # 这道题先按k=1生成所有的abbr。然后对于每个abbr，找到后面跟它相同的abbr，然后把他们的前缀全部+1，再检查还有多少个重复的
        # 重复这个过程，直到没有人再和ans[i]重复。
        prefix = [1]*len(D)
        ans = [Abbr(D[i], 1) for i in range(len(D))]
        for i in range(len(D)):
            while True:
                same_prefix = set() # 存放所有和ans[i]重复的ans[j]，把下标放进一个set
                for j in range(i+1, len(D)):
                    if ans[j]==ans[i]:
                        same_prefix.add(j)
                if len(same_prefix)==0: break
                same_prefix.add(i) # 把自己也放进set
                for abb in same_prefix: # 对于set中的所有人，把prefix+1，再重复这个过程
                    ans[abb] = Abbr(D[abb], prefix[abb]+1)
                    prefix[abb] += 1
        return ans