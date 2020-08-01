class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 先按元素长度排序，因为长的word只能由短的word组成
        # 对每一word，set=之前的所有word，对这个word做Word Break题的相同DP操作
        # 每个word都做一次，相当于Word Break的扩展
        words = sorted(words, key = lambda x:len(x))
        # print(words)
        seen = set()
        ans = []
        
        for w in words:
            dp = [True]
            for i in range(len(w)):
                dp.append(False)
                for j in range(i+1):
                    val = dp[j] and w[j:i+1] in seen
                    if val:
                        dp[-1] = True
                        break
            if dp[-1] and len(w)>0: ans.append(w)
            
            seen.add(w)
        return ans