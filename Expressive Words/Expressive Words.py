class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        # 4 pointers。s的group长度如果>=3，那么w对应的group长度只要小于s就可以。
        # 如果s的group长度<3，那么w对应的group长度必须和s一样
        # 此外还要注意对应字符是否相等，以及s或w指针是否同时到达终点
        def helper(s, w):
            si, sj, wi, wj = 0,0,0,0
            while sj<len(S) and wj<len(w):
                while sj<len(s) and s[sj]==s[si]: sj+=1
                while wj<len(w) and w[wj]==w[wi]: wj+=1
                if s[si]!=w[wi]: return 0
                if wj-wi>sj-si: return 0
                if sj-si<3 and sj-si!=wj-wi: return 0
                si, wi = sj, wj
            
            if sj==len(s) and wj==len(w): return 1
            return 0
        
        ans = 0
        for w in words:
            ans += helper(S, w)
        return ans